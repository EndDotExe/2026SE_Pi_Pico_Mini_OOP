from led_light import Led_light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem, Controller
from time import sleep, time

debug = False

# pedestrian lights
led_pedestrian_red = Led_light(19, True, True)
led_pedestrian_green = Led_light(17, False, True)

# traffic lights
led_traffic_red = Led_light(3, False, True)
led_traffic_amber = Led_light(5, False, True)
led_traffic_green = Led_light(6, False, True)

# button stuff
pedestrian_button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)

driver = TrafficLightSubsystem(led_traffic_red, led_traffic_amber, led_traffic_green, False)
walkers = PedestrianSubsystem(led_pedestrian_red, led_pedestrian_green, pedestrian_button, buzzer)
control = Controller(led_pedestrian_red, led_pedestrian_green, led_traffic_green, led_traffic_amber, led_traffic_red, pedestrian_button, buzzer, True)

while True:
    control.update
    sleep(0.1)