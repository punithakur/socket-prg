import socket
import time
import threading

s=socket.socket()
s.connect((socket.gethostname(), 20000))
while True:
    data=s.recv(1024)
    print("msg from server",(data).decode())
    s.send(input("input---->").encode())
