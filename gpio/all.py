import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 18
GPIO.setup(led_pin, GPIO.OUT)

switch_pin = 23 
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(switch_pin) == False:
            GPIO.output(led_pin, True)
        else:
            GPIO.output(led_pin, False)
finally:
    print("Cleaning up")
    GPIO.cleanup()
