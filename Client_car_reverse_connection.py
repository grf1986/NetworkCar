import socket
import time
import json




#variables
host = "192.168.0.101"
port = 65432

Button_List = []

Joypad_left_button = 1
Joypad_left_button_stop_value = "0"
Joypad_left_button_back_value = range(-1,-9,-1)


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


class client(object):


    def forward(self):
        print("Going forwards")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)
        
        

    def stop(self):
        print("Stop")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.LOW)
        

    def backward(self):
        print("Going backwards")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.LOW)

        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.LOW)
    

    def cleanup(self):
        GPIO.cleanup()


    
    def connect(self):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host,port))
                #s.send(conn_key)
                data  = s.recv(1024).decode("utf-8")
                y = json.loads(data)

                button_id = y["id"]
                button_value_drive = y["Value"]
            
                if button_id == Joypad_left_button and int(button_value_drive) > 2:
                    self.forward()

                if button_id == Joypad_left_button and int(button_value_drive) == 0:
                    self.stop()

                if button_id == Joypad_left_button and int(button_value_drive) < 0:
                    self.backward()
                    
                    
            except Exception as e:
                print("reconnecting.....")
                time.sleep(0.75)
                self.connect()
                pass
                

def main():
    Client = client()
    Client.connect()
    client.cleanup()



if __name__ == "__main__":
    main()