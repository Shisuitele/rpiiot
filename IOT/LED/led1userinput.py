import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode
x=int(input("Enter no.of pins"))
GPIO.setup(x,GPIO.OUT)
GPIO.output(x,False)
while True:
    GPIO.output(x,True)