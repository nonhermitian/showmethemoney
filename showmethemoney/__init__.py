# This code is part of showmethemoney
#
# (C) Copyright IBM, Paul D. Nation, 2022
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""showmethemoney
"""

try:
    from .version import version as __version__
except ImportError:
    __version__ = '0.0.0'

from ._cost import estimate_cost


def about():
    """The showmethemoney version info function.
    """
    print('='*80)
    print('# showmethemoney version {}'.format(__version__))
    print('# (C) Copyright Paul D. Nation, 2022.')
    print('='*80)
