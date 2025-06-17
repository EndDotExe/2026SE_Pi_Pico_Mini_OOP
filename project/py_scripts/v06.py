from audio_notification import Audio_Notification
from machine import Pin
from time import sleep

audio = Audio_Notification()


# testing warning_on()
print("Testing: warning_on()")
warning_on()
sleep(0.1)
