"""A Test dvs_printf Package."""
from .__printf__ import printf as pf
# from __printf__ import printf as pf

class init:
    def __init__(self, 
    style:str|None='typing', speed:int|None=3, interval:int|None=2, stay:bool|None=True,
    getMat:bool|None=False):
        """
`initializer for dvs_printf setter method`

set_style    
    to set the style of printf animation function
   Style list => [typing, headline, newsline, mid, f2b, b2f, gunshort, snip,
    left, right, center, centerAC, centerAL, centerAR, matrix, matrix2, help]
set_speed    
    to set the speed of printf animation from (1 to 6)
set_interval     
    to set the interval time between 2 stream animation animation
set_stay    
    to set the stay for printf animation

---

### default pramiters

style
    different type of printing styles animation, default  `style="typing"`.
    ```python
    Style_list: [typing, headline, newsline, mid, f2b, b2f, gunshort, snip, 
    left, right, center, centerAC, centerAL, centerAR, matrix, matrix2, help]
    ```
speed
   speed of printf animation from 1 to 6, `default speed=3`.
interval
   waiting time between two lines, `default interval=2`.
stay
   after animation whether you want the stream OR NOT, 
   `default stay=True`.

`style="help" for more info`.
        """

        self._style=self.style_setter=style
        self._speed=self.speed_setter=speed
        self._interval=self.interval_setter=interval
        self._stay=self.stay_setter=stay
        self._getMat=self.getMat_setter=getMat
        
        
        

    @property
    def set_style(self) -> str:
        """different type of printing animation styles.
        ```python
        [typing, headline, newsline, mid, f2b, b2f, gunshort, snip, left, right,
          center, centerAC, centerAL, centerAR, matrix, matrix2, help]
        ```"""
        return self.style_setter
    
    @set_style.setter
    def set_style(self, value):
        self.style_setter = value


    @property
    def set_speed(self) -> int:
        "set animation speed from (1 to 6) integer"
        return self.speed_setter
    
    @set_speed.setter
    def set_speed(self, value):
        self.speed_setter = value


    @property
    def set_interval(self) -> int:
        """interval time between 2 value animations.

        time in seconds `(integer) shoud be >= 0 or greater`
        """
        return self.interval_setter
    
    @set_interval.setter
    def set_interval(self, value):
        if (type(value) == int or float) and value>=0:
            self.interval_setter = value

    
    @property
    def set_stay(self) -> str:
        """after animation whether you want the stream OR NOT, 
        
        default  `stay=True`"""
        return self.stay_setter
    
    @set_stay.setter
    def set_stay(self, value):
        if value==True or value==False:
            self.stay_setter = value
 

    "test property"
    @property
    def set_getMat(self) -> bool | str :
        '''for metrices'''
        return self.getMat_setter
    
    @set_getMat.setter
    def set_getMat(self, value):
        self.getMat_setter = value



    def printf(self, *values:any,
        style: str | None = None, 
        speed: int | None = None, 
     interval: int | None = None,
        stay: bool | None = None,
      getMat: bool | str | None = None ):
        ''' 
    ```python 

(method) def printf(
    self: Self@init, 
    *values : any, 
    style : str | None = 'typing', 
    speed : int | None = 3, 
    interval : int | None = 2, 
    stay : bool | str | None = True
) -> None :
    ```
---

defaults are None to make this module `more dynamic`.

prints values to a stream. 

style
   different type if printing styles animation, default  `style="typing"`.
speed
   speed of printf animation from 1 to 6, default `speed=3`.
interval
   waiting time between two lines, default  `interval=2`.
stay
   after animation whether you want the stream OR NOT, 
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
        if (getMat==None)and(self.getMat_setter!=
        self._getMat):self._getMat=self.set_getMat
        elif getMat!=None:self._getMat=getMat 

        pf(values,
            style=self._style,
            speed=self._speed,
            interval=self._interval,
            stay=self._stay,
            getMat=self._getMat,
            )
        