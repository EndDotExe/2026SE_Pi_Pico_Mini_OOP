from lib import pedestrian_button
from machine import Pin
import time

pedestrian = pedestrian_button.Pedestrian_Button

# check button_state()
print("Testing: button_state")
button_state()
print("( :3 )")


# check callback info
print("Testing: callback()")
pedestrian_button.callback()


# thats the only function in the class what do i do......