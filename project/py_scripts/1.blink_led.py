from machine import Pin
from time import sleep

#have a little delay
sleep(0.1)

led_pin = 25

led = Pin(led_pin, Pin.OUT)

while True:
    led.value(True)
    sleep(1)
    led.value(False)
    sleep(1)