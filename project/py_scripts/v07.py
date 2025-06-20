from led_light import Led_light
from pedestrian_button import Pedestrian_Button
from audio_notification import Audio_Notification
from controller import TrafficLightSubsystem, PedestrianSubsystem
from time import sleep, time

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

def Traffic_Subsystem_driver():
# Red light test
    print("Testing Traffic Light In 3 seconds")
    sleep(3)
    driver.show_red()
    print("Pass if: Red ON, Amber OFF, Green OFF")
    sleep(2)

# Amber light test
    print("Testing Traffic Light In 3 seconds")
    sleep(3)
    driver.show_amber()
    print("Pass if: Red OFF, Amber ON, Green OFF")
    sleep(2)

# Green light test
    print("Testing Traffic Light In 3 seconds")
    sleep(3)
    driver.show_green()
    print("Pass if: Red OFF, Amber OFF, Green ON")
    sleep(2)

Traffic_Subsystem_driver()
sleep(1)

def Pedestrian_Subsystem_driver():
    # Green Light test
    print("Testing pedestrian light in 3 seconds")
    sleep(3)
    walkers.show_walk
    print("Pass if Green ON, Red OFF & NOT Flashing")
    sleep(2)

    print("Testing pedestrian light in 3 seconds")
    sleep(3)
    walkers.show_stop
    print("Pass if Green OFF, Red ON & NOT Flashing")
    sleep(2)

    print("Testing pedestrian light in 3 seconds")
    sleep(3)
    walkers.show_warning
    print("Pass if Green OFF, Red ON & FLASHING")
    sleep(2)

Pedestrian_Subsystem_driver()