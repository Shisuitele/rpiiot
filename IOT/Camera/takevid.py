#takevid

import picamera
import time

cam=picamera.PiCamera()

cam.resolution(1024,720)
cam.brightness = 60

#start recording
cam.start_recording("/home/pi/vid_nilesh.h264")

#wait for vid recording

cam.wait_recording(20)

#stop recording

cam.stop_recording()
cam.close()

print("recording stopped")