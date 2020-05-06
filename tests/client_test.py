
import socket
import json

host = "localhost"  # Standard loopback interface address (localhost)
port = 8888        # Port to listen on (non-privileged ports are > 1023)




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
data  = s.recv(1024).decode("utf-8")


# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(data)

# the result is a Python dictionary:
print(y["id"])

if y["Value"] < 0:
    print("kleiner")

# print(data)
