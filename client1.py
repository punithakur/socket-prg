import socket
import time
import threading

s=socket.socket()
s.connect((socket.gethostname(), 20000))
while True:
    
    s.send(input("input---->").encode())
    '''
    data=s.recv(1024)
    print((data).decode())
    '''
s.close()