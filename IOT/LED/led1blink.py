import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,False)
while True:
    GPIO.output(8,False)
    time.sleep(1)
    GPIO.output(8,True)
    time.sleep(1)