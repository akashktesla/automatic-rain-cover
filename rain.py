import RPi.GPIO as GPIO
import time
from time import sleep
from math import pi

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25,GPIO.IN)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#GPIO.setup(24,GPIO.OUT)
#GPIO.output(24, True)


def minimumRotations(length,r,th):

    #pi = 3.141592
    temp = 0
    rotation = 0
    #circumfrence
    while(temp<length):
        #print('loop')
        cfren = 2*pi*(r+th)
        r = r+th
        print('cfren: {cfren}')
        bla= temp
        print(bla)
        temp = temp +cfren

        rotation+=1
        print(f'temp: {temp}')
    
    returns = (rotation-1) + (length-bla)/cfren
    return returns

def timeTaken(rpm,rotation,ftl):

    #defining the variable
    rps = rpm/60
    #converting rpm to rps
    timeT = (1/rps)*rotation
    #calculating the time taken
    return timeT+timeT*(ftl/100)

rpm = 60;
#rotation per minute
length =2;
#length in meters
r = 0.1;
#radius of the pipe in meters
th = 0.02
#ftl - frictional time loss in %
ftl = 5
rot = minimumRotations(length,r,th)
print(f'minimum rotations: {rot}')
#tt - total time
tt = timeTaken(rpm,rot,ftl)
print(f'time taken: {tt}')
#converting seconds into milliseconds
#tt = tt*1000
#defining the threshold
threshold = 3
tt = 1.9
#always active
flaga = True
flagb = False



while True:
    #print(GPIO.input(23))
    if(GPIO.input(25) == 0): 
        if (flaga):
            print('rain is detected')
            print('in1 set as high')
            print('in2 set as low')
            print('motor is rotating clockwise the device is on')
            GPIO.output(23, True)
            print(tt)
            sleep(tt)
            
            flaga = False
            flagb = True
            
            GPIO.output(23, False)
            sleep(5)
            print('testing 1')
    
    if(GPIO.input(25)  == 1): 
        if (flagb):
            print('rain is not detected')
            print('in1 set as low')
            print('in2 set as high')
            print('motor is rotating counter clockwise the device is off')
            sleep(threshold)
            GPIO.output(24, True)
            sleep(tt)
            flaga = True
            flagb = False
            GPIO.output(24, False)
            sleep(5)
#print(input)
'''
while True:
  if (GPIO.input(23)):
    print("it's not raining")
  else:
      print(" raining")

'''