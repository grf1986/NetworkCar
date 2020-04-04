import socket
import time



#variables
host = "localhost"
port = 65432
conn_key = "jhhgefghchcc"
LB_press = "12,1"
LB_release ="12,0"
RB_press = "13,1"
RB_release = "13,0"
Y_button_press = "10,1"
Y_button_release = "10,0"
B_Button_press = "7,1"
B_Button_release = "7,0"
A_Button_press = "6,1"
A_Button_release = "6,0"
X_Button_press = "9,1"
X_Button_release = "9,0"

D_pad_left_press ="17,(-1, 0)"
D_pad_left_release ="17,(0, 0)"
D_pad_up_press ="17,(0, 1)"
D_pad_up_release ="17,(0, 0)"
D_pad_right_press ="17,(1, 0)"
D_pad_right_release ="17,(0, 0)"
D_pad_down_press ="17,(0, -1)"
D_pad_down_release ="17,(0, 0)"


class client(object):
    
    def connect(self):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host,port))
                #s.send(conn_key)
                data = s.recv(2024).decode("utf-8")
                #print(data)
                if data in LB_press:
                    print("LB pressed")
                elif data in LB_release:
                    print("LB relesed")
                elif data in RB_press:
                    print("RB pressed")
                elif data in RB_release:
                    print("RB released")
                elif data in Y_button_press:
                    print("Y button pressed")
                elif data in Y_button_release:
                    print("Y button released")
                elif data in B_Button_press:
                    print("B button pressed")
                elif data in B_Button_release:
                    print("B button released")
                elif data in A_Button_press:
                    print("A button is pressed")
                elif data in A_Button_release:
                    print("A button released")
                elif data in X_Button_press:
                    print("X button pressed")
                elif data in X_Button_release:
                    print("X button released")

                elif data in D_pad_left_press:
                    print("Left D pad pressed")
                elif data in D_pad_left_release:
                    print("Left D pad released")
                elif data in D_pad_up_press:
                    print("Up D pad pressed")
                elif data in D_pad_up_release:
                    print("up D pad relesed")
                elif data in D_pad_right_press:
                    print("Right D pad pressed")
                elif data in D_pad_right_release:
                    print("Right D pad released")
                elif data in D_pad_down_press:
                    print("Down D pad pressed")
                elif data in D_pad_down_release:
                    print("Down D pad released")

                else:
                    print("Function not mapped yet :)")
                    

                
                    


            except Exception as e:
                print("could not connect to RC car, reconnecting....",e)
                time.sleep(5)
                self.connect()

def main():
    Client = client()
    Client.connect()


if __name__ == "__main__":
    main()