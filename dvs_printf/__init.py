"""A Test dvs_printf Package."""
from .__printf__ import printf as pf

class init:
    def __init__(self, 
    style:str|None='typing', speed:int|None=3, interval:int|None=2, stay:bool|None=True,
    getmat:bool|None=False):
        """
`dvs_printf initializer`, preset parameters for printf

init.printf(values, ..., keywords)
    only callable function in init
set_style    
    to set the style animation for printf function 
set_speed    
    to set the speed of printf animation from (1 to 6)
set_interval     
    to set the interval time between 2 values animation animation
set_stay    
    to set the stay parameter for printf animation
set_getmat   
    to set the getmat for matrices for printf and listfunction

---
---

### default pramiters

#### style
    different type of printing styles animation, default  `style="typing"`.
     Style_list: -> [typing, headline, newsline, mid, f2b, b2f, gunshort, snip, 
    left, right, center, centerAC, centerAL, centerAR, matrix, matrix2, help]
#### speed
   speed of printf animation from 1 to 6, `default speed=3`.
#### interval
   waiting time between two lines, `default interval=2`.
    (interval in seconds >= 0)
#### stay
   after animation whether you want the values OR NOT, 
    `default stay=True`.
#### getmat
    if values is matrix, set getmat=True. `default getmat=False`
     getmat can be `True`, `"true"`, 
    and `"show"` for matrix info <class, shape, dtype>

`style="help" for more info`.
        """
        self._style=self.style_setter=style
        self._speed=self.speed_setter=speed
        self._interval=self.interval_setter=interval
        self._stay=self.stay_setter=stay
        self._getmat=self.getmat_setter=getmat
        

    @property
    def set_style(self) -> str:
        """different type of printing animation styles.\\
        [  typing, headline, newsline, mid, f2b, b2f, gunshort, snip, left, \\
        right, center, centerAC, centerAL, centerAR, matrix, matrix2, help]"""
        return self.style_setter
    @set_style.setter
    def set_style(self, value):
        self.style_setter = value

    @property
    def set_speed(self) -> int | float:
        "set animation speed from (1 to 6) [integer | float]"
        return self.speed_setter
    @set_speed.setter
    def set_speed(self, value):
        self.speed_setter = value

    @property
    def set_interval(self) -> int | float:
        """interval time between 2 value animations. \\
        time in seconds `(integer | float) shoud be >= 0`"""
        return self.interval_setter
    @set_interval.setter
    def set_interval(self, value):
        if (type(value) == int or float) and value>=0:
            self.interval_setter = value

    @property
    def set_stay(self) -> bool:
        """after animation whether you want the values on stream OR NOT. \\
        default  `stay=True`"""
        return self.stay_setter
    @set_stay.setter
    def set_stay(self, value):
        if value==True or value==False:
            self.stay_setter = value
 
    @property
    def set_getmat(self) -> bool | str :
        '''matrix data modifier for `pytorch, tensorflow, numpy, pandas, list` \\
        for animation, `default getmat=False`, set as `(True, "true", "show")`'''
        return self.getmat_setter
    @set_getmat.setter
    def set_getmat(self, value):
        self.getmat_setter = value

    def printf(self, *values:any,
        style: str | None = None, 
        speed: int | float | None = None, 
     interval: int | float | None= None,
        stay: bool | None = None,
      getmat: bool | str | None = None ) -> None:
        ''' 
    ```python 

def printf(
    * values: any , 
       style: str |      None = 'typing', 
       speed: int |float|None = 3, 
    interval: int |float|None = 2, 
        stay: bool|      None = True,
      getmat: bool| str |None = None ) -> None :
    ```
---
---

defaults are None to make this module more dynamic.

prints values to a stream with animation. 

style
   different types of print animation styles, default  `style="typing"`.
speed
   speed of printf animation from 1 to 6, default `speed=3`.
interval
   waiting time between two lines, default  `interval=2`.
stay
   after animation whether you want the values OR NOT, 
   default  `stay=True`.

`style="help" for more info`.
        '''

        if (style==None)and(self.style_setter!=
        self._style):self._style=self.set_style 
        elif style!=None:self._style=style 
        if (speed==None)and(self.speed_setter!=
        self._speed):self._speed=self.set_speed 
        elif speed!=None:self._speed=speed
        if (interval==None)and(self.interval_setter!=
        self._interval):self._interval=self.set_interval 
        elif interval!=None:self._interval=interval
        if (stay==None)and(self.stay_setter!=
        self._stay):self._stay=self.set_stay
        elif stay!=None:self._stay=stay 
        if (getmat==None)and(self.getmat_setter!=
        self._getmat):self._getmat=self.set_getmat
        elif getmat!=None:self._getmat=getmat 

        pf(values,
            style=self._style,
            speed=self._speed,
            interval=self._interval,
            stay=self._stay,
            getmat=self._getmat,
            )
        
