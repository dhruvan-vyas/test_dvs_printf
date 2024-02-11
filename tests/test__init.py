import dvs_printf


def test_init():
    pf = dvs_printf.__init()
    printf = pf.printf

    assert pf.set_style == "typing" 
    assert pf.set_speed == 3
    assert pf.set_interval == 2
    assert pf.set_stay == True
    assert pf.set_getMat == False

    pf = dvs_printf.__init(style="left",
    speed=2, interval=1, stay=False, getMat=True)
    assert pf.set_style == "left" 
    assert pf.set_speed == 2
    assert pf.set_interval == 1
    assert pf.set_stay == False
    assert pf.set_getMat == True

    pf.set_style = "gunshort"
    pf.set_speed = 6
    pf.set_interval = 3
    pf.set_stay = True
    pf.set_getMat = "true"
    printf("hello world", style="mid",
    speed=4, interval=.5, stay=False, getMat="show")

    assert pf.set_style == "gunshort"
    assert pf.set_speed == 6
    assert pf.set_interval == 3
    assert pf.set_stay == True
    assert pf.set_getMat == "true"

    




