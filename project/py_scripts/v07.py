from controller import TrafficLightSubsystem, PedestrianSubsystem
from led_light import Led_light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep, time

led_pedestrian_red = Led_light(19, True, True)
led_pedestrian_green = Led_light(17, False, True)
led_traffic_red = Led_light(3, False, True)
led_traffic_amber = Led_light(5, False, True)
led_traffic_green = Led_light(6, False, True)
pedestrian_button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)


def Subsystem_driver():
    # 


# Subsystem_driver()