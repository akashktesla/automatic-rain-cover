import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay1 = 24
relay2 = 23
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)

while True:
    cmd = input('>>>')
    if cmd == 'on':
        GPIO.output(relay2,False)
    if cmd == 'off':
        GPIO.output(relay1,False)
        GPIO.output(relay2,False)
    if cmd == 'cw':
        GPIO.output(relay1,True)
        GPIO.output(relay2,False)
        sleep(1.9)
        GPIO.output(relay1,False)
        GPIO.output(relay2,False)
        
        
    if cmd == 'acw':
        GPIO.output(relay1,False)
        GPIO.output(relay2,True)
        sleep(1.9)
        GPIO.output(relay1,False)
        GPIO.output(relay2,False)
