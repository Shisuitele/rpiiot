import RPi.GPIO as GPIO
import time

i=1
nt=int(input("Enter no.of times to blink"))
s=int(input("At what speed to blink"))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

def blink(nt,s):
    for i in range(0,nt):
        GPIO.output(5,True)
        print(i+1)
        GPIO.output(10,True)
        print(i+1)
        GPIO.output(13,True)
        print(i+1)
        GPIO.output(19,True)
        print(i+1)
        GPIO.output(26,True)
        print(i+1)

        GPIO.output(5,False)
        print(i+1)
        time.sleep(speed)
        GPIO.output(10,False)
        print(i+1)
        time.sleep(speed)
        GPIO.output(13,False)
        print(i+1)
        time.sleep(speed)
        GPIO.output(19,False)
        print(i+1)
        time.sleep(speed)
        GPIO.output(26,False)
        print(i+1)
        time.sleep(speed)

blink(nt,s)
print("Done")