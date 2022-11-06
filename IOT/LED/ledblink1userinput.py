import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
x=int(input("Enter the pin"))
t=int(input("Enter the sleep time"))
GPIO.setup(x,GPIO.OUT)
GPIO.output(x,False)
while True:
    GPIO.output(x,False)
    time.sleep(t)
    GPIO.output(x,True)
    time.sleep(t)