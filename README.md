# showmethemoney

`showmethemoney` is a tool for esimating the cost of running circuit using the Qiskit Runtime on the IBM Cloud.  **This is only a rough approximation** and should be, at best, considered a lower bound.

## Installation

```
pip install showmethemoney
```


## Usage

`showmethemoney` is really easy to use as it has a single function that takes one or more circuits and a backend and returns the cost.  There are several configurable inputs as well

```python

import showmethemoney as smtm
smtm.estimate_cost(qc, backend)

```

For example, A QV circuit executed 4000 times, and transpiled in the Runtime can be computed like

```python
from qiskit.circuit.library import QuantumVolume
from qiskit.providers.fake_provider import FakeBoeblingen

import showmethemoney as smtm

backend = FakeBoeblingen()

qc = QuantumVolume(7)
qc.measure_all()

smtm.estimate_cost(qc, backend)
```

returning

```python
15.494356116334012
```

indicating that it costs roughly 15 USD to execute one QV circuit 4000 times.  The actual cost will vary someone depending on the computer on which the estimate is run, and the variability inherent in some of the stochastic compilation pieces.
