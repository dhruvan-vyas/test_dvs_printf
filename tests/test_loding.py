from dvs_printf import showLoding
import time

def test_SleepLoging():
    showLoding(target=time.sleep,
        args = (3 , ),
        lodingText="Loding",
        lodingChar="◼︎"   
    )

