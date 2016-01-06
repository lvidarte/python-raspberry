import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(5)
    camera.capture('image.jpg')
    camera.stop_preview()
