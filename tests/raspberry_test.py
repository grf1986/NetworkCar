import RPi.GPIO as GPIO
from time import sleep
import time 

#setmode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Variables
Motor1A = 20
Motor1B = 22
Motor1E = 23
Motor2A = 24
Motor2B = 21
Motor2E = 19

#Setup GPIO pins
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

class Car(object):

    
    def forward(self):
        print "Going forwards"
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)
        

    def stop(self):
        print("going low")
        #set all GPIO to low
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.LOW)
        time.sleep(3)

    def backward(self):
        print ("Going backwards")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.LOW)

        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.LOW)
    

    def cleanup(self):
        GPIO.cleanup()


Move = Car()
try:
    Move.forward()
    time.sleep(5)
    Move.stop()
    time.sleep(5)
    Move.backward()
    time.sleep(5)
    Move.stop()

    #Move.cleanup()
except Exception as e:
    print("There was a error " , e)
