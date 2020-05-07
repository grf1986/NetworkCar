import socket
import time
import json




#variables
host = "192.168.0.101"
port = 65432

Button_List = []

# LB_press = "12,1"
# LB_release ="12,0"
# RB_press = "13,1"
# RB_release = "13,0"
# Y_button_press = "10,1"
# Y_button_release = "10,0"
# B_Button_press = "7,1"
# B_Button_release = "7,0"
# A_Button_press = "6,1"
# A_Button_release = "6,0"
# X_Button_press = "9,1"
# X_Button_release = "9,0"

# D_pad_left_press ="17,(-1, 0)"
# #D_pad_left_release ="17,(0, 0)"
# D_pad_up_press ="17,(0, 1)"
# D_pad_up_release ="17,(0, 0)"
# D_pad_right_press ="17,(1, 0)"
# #D_pad_right_release ="17,(0, 0)"
# D_pad_down_press ="17,(0, -1)"
# #D_pad_down_release ="17,(0, 0)"

steer_left = range(1,180,1)
steer_right = range(-1,-180,-1)
Joypad_left_button = 1
Joypad_right_button =2
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
                button_stear_value = y["Value"]

            
                if button_id == Joypad_left_button and int(button_value_drive) > 2:
                    self.forward()

                if button_id == Joypad_left_button and int(button_value_drive) == 0:
                    self.stop()

                if button_id == Joypad_left_button and int(button_value_drive) < 0:
                    self.backward()

                if button_id == Joypad_right_button and int(button_stear_value) in steer_left:
                    print("turning left")
                
                if button_id == Joypad_right_button and int(button_stear_value) in steer_right:
                    print("turning right")
                    
            except Exception as e:
                print("reconnecting.....")
                time.sleep(0.75)
                self.connect()
                
                

def main():
    Client = client()
    Client.connect()
    client.cleanup()



if __name__ == "__main__":
    main()