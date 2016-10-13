"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import picamera
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

switch_pin = 23 
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        while True:
            if GPIO.input(switch_pin) == False:
                print("Taking photo")
                camera.capture('image.jpg')
finally:
    print("Cleaning up")
    camera.stop_preview()
    GPIO.cleanup()
