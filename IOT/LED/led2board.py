# 2 led glow in BOARD mode
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.output(15,False)
GPIO.output(18,False)
while True:
    GPIO.output(15,True)
    PIO.output(18,True)