#write a program to glow the LED at pin 9 in BOARD mode 1 pin

import RPi.GPIO as GPIO
GPIO.setwarning(false)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,False)
while True:
    GPIO.output(8,True)