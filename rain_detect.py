import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

rain = 25

GPIO.setup(rain,GPIO.IN)
flaga = True
flagb = False

while True:
   if(GPIO.input(rain) == 0) and flaga :
      print('rain is detected')
      flagb = True
      flaga = False
      sleep(2)  
   elif(GPIO.input(rain)==1) and flagb :
      print('rain not detected')
      flaga = True
      flagb = False
      sleep(2)
