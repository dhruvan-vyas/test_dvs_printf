"""
[dvs_printf](https://google.com) module. A simple and dynamic pritning animation function for python.

Using printf function of this modyul you to create nice & clean printing animation in \\
terminal-based python project.suport any Data type. IF `list, set, tuple, dict` \\
is given Then the output animation work with each items. 

module can create different printing animation useing listed Styles \\
`[typing, headline, newsline, mid, gunshort, snip, matrix, matrix2,` \\
`left, right, center, centerAC, centerAL, centerAR, f2b, b2f, help]` 

---
### Module include functions
+ [printf](https://google.com): the core of the module. use to create animation
+ [init](https://google.com): A dynamic initializer for printf that allows users to preset parameters
+ [showLoding](https://google.com): create Loding bar with backgrond function runner
+ [listfunction](https://google.com): An additional function used by printf to create list[str] based on input values.
"""


__all__ = ("init", "printf", "listfunction", "showLoding") 

from .__printf__ import printf, listfunction
from .__init import init
from .Loding import showLoding
