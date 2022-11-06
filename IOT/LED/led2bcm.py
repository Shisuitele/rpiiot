#2 pin BCM
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(23,False)
GPIO.output(27,False)
while True:
    GPIO.output(23,True)
    GPIO.output(27,True)