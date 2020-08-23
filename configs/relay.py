import RPi.GPIO as GPIO
from time import sleep

relay_pin_1 = 6
relay_pin_2 = 13
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#relay
GPIO.setup(relay_pin_1,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(relay_pin_2,GPIO.OUT, initial=GPIO.HIGH)
def door_open(unlock_time):
    GPIO.output(relay_pin_1,GPIO.HIGH)
    GPIO.output(relay_pin_2,GPIO.LOW)
    print('Door unlocked')
    sleep(unlock_time)
    GPIO.output(relay_pin_1,GPIO.LOW)
    GPIO.output(relay_pin_2,GPIO.HIGH)
    print('Door locked')
    
def door_status():
    if GPIO.input(relay_pin_1) == GPIO.LOW and GPIO.input(relay_pin_2) == GPIO.HIGH:
        return "LOCKED"
    elif GPIO.input(relay_pin_1) == GPIO.HIGH and GPIO.input(relay_pin_2) == GPIO.LOW:
        return "UNLOCKED"
    else:
        return "Something went wrong"
