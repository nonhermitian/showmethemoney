# This code is part of Showmethemoney.
#
# (C) Paul D. Nation, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""Compute cost"""
from qiskit import transpile
from time import perf_counter


def estimate_cost(circuits, backend, shots=4000,
                  transpiler_config={'optimization_level': 1},
                  skip_transpilation=False,
                  runtime_cost=1.6,
                  constant_offset=10.0,
                  ):
    """Estimates the cost of sending one or more circuits to the Qiskit Runtime via the IBM Cloud
    
    Parameters:
        circuits (QuantumCircuit or list): One or more QuantumCircuits
        backend (IBMBackend): The target system
        shots (int): Number of shots per circuit, default is 4000
        transpiler_config (dict): Transpiler configuration
        runtime_cost (float): The cost per second in Dollars for Runtime
        constant_offset (float): The service overhead, i.e. the cost of doing nothing, default is 10.0
        
    Returns:
        float: The total estimated cost
        
    Notes:
        This is a rough lower bound on the cost of a Runtime job on IBM Cloud.  It is just an
        educated guess to give you some idea before you execute.
    """
    if not isinstance(circuits, list):
        circuits = [circuits]
    config = backend.configuration()   
    transpilation_time = 0
    if not skip_transpilation:
        trans_start = perf_counter()
        trans_circuits = transpile(circuits, backend, scheduling_method='alap', **transpiler_config)
        trans_end = perf_counter()
        transpilation_time += trans_end - trans_start
    else:
        trans_circuits = circuits
    schedule_start = perf_counter()
    trans_circuits = transpile(circuits, backend, optimization_level=0, scheduling_method='alap')
    schedule_end = perf_counter()
    schedule_time = schedule_end - schedule_start
    raw_executation_time = 0
    for qc in trans_circuits: 
        raw_executation_time += (qc.duration * config.dt + config.default_rep_delay + 10e-9)*shots
    # Here the factor of 10 for the schedule time is just a horrible approximation to the
    # waveform generation time
    total_cost = (transpilation_time + raw_executation_time + 10*schedule_time) * runtime_cost
    return (total_cost + constant_offset)