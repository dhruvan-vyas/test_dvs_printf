"""
dvs_printf Package. 
A simple and dynamic pritning animation styles for python.

Using printf function of this modyul you to create nice & clean printing animation
 in terminal on your python project.

this module create different Types of printing animation Styles. listed below
 `[typing, headline, newsline, mid, gunshort, snip,left, right, 
 center, centerAC, centerAL, centerAR, matrix, matrix2, f2b, b2f, help]`

it suport any Data type. IF `list, set, tuple or dict` is given Then
 the output animation work with each items in `list, set, tuple or dict`.
"""
# __all__ = ("printf", "listfunction", "init","showLoding")

from .__printf__ import printf, listfunction
from .__init import init
from .Loding import showLoding

# from __printf__ import printf, listfunction
# from __init import init
# from Loding import showLoding
#------------------( readme for loding )----------------------

"""
create loding bar in terminal with `threading` for 

* `waiting time for downlod files` 
* `run other function and wait till finish`
* `import other functions`
* `waiting for interner conection`

-----------------------------------------------------

loding funtion works on threading module 
 so, it's `take same input as threading`.

#### target
  the target `object` or `function` to work in background.

#### args
   the argument that `target function taks` 
    in `tuple` `args=(1,2,3)`
```  
  But if `there is just one argument` 
  add coma at the and 
```
   args=(1`,`)

#### kwargs
   the key words that `target function taks` 
  ``` python
   data type(dict)
  kwargs = {"values_1": 1, "values_2": "hello world"}
  ```

#### lodingText
  text befor loding bar `loding[####......]`

#### lodingCher
  cheractor to see progresd loding bar
    any `one cher in string`

#### unlodCher
  cherector to see unprogresed loding bar
   any `one cher in string`
 
    """



