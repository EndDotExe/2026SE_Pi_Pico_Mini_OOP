from time import sleep
from machine import Pin
from pedestrian_button import Pedestrian_Button


button = Pedestrian_Button

# check button_state()
print("Testing: button_state()")
button.button_state()
print(button.button_state())


# check callback info
print("Testing: callback()")
button.callback()
print(button.current_time)
