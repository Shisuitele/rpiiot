#Take Pic

import picamera
import time

cam=picamera.PiCamera()

cam.resolution(1024,720)
cam.brightness = 60

#preview
cam.start_preview()

#add txt on the image

cam.annotate_text = "Hey There!"
time.sleep(5)
#save img

cam.capture("home/pi/nilesh.jpeg")
cam.stop_preview()

