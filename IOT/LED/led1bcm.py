#BCM 1 pin
import RPi.GPIO as GPIO
GPIO.setwarnings(false)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14,GPIO.OUT)
GPIO.output(14,False)
while True:
    GPIO.output(14,True)