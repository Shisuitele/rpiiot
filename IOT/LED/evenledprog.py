import RPi.GPIO as GPIO
import time
x=int(input("Enter a pin no"))
if(x%2==0):
    print("led will blink")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(x,False)
    while True:
        GPIO.output(x,False)
        time.sleep(1)
        GPIO.output(x,True)
        time.sleep(1)
else:
    print("Led can't blink")