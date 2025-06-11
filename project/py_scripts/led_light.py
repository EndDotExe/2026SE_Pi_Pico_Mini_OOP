from led_light import Led_light
from machine import Pin
from time import sleep, time

sleep(1)



led = Led_light(3, flashing=True, debug=True)

# check on()
print("Testing: on() ")
led.on()
if led.value == 1:
    print("Led should be on")
sleep(0.5)

# check off()
print("Testing: off()")
led.off()
if led.value == 0:
    print("LED should be off")
sleep(0.5)

# check toggle - on
print("Testing: toggle()")
led.toggle()
if led.value == 1:
    print("Test passed - Toggle: on()")
sleep(0.5)

# check toggle - off
print("Testing: toggle()")
led.toggle()
if led.value == 0:
    print("Test passed - Toggle: off()")
sleep(0.5)