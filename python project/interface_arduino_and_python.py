'''
1st : aurdino should manage lib ctrl + shift  + i seacrch for firmataExpress and install
pip install in pycharm pymata4 or python package pymata4 

'''

import time
from pymata4 import pymata4

triggerPin = 12
echo_pin = 13
board = pymata4.Pymata4()

def the_callback(data):
    print("distance : ", data[2])

board.set_pin_mode_sonar(triggerPin,echo_pin, the_callback)

while True:
    try:
        time.sleep(1)
        board.sonar_read(triggerPin)
    except Exception:
        board.shutdown()
