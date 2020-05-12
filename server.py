import socket
import threading

s=socket.socket()
s.bind((socket.gethostname(),20000))
list_con=[]
list_add=[]
s.listen(5)
global f
f=1
def accepting():
    
    while True:
        
        global f
        conn , add = s.accept()
        
        list_con.append(conn)
        list_add.append(add)
        if f==1:
            t2.start()
            f+=2
            
       
def listing():
    print("select client to send msg")
    for j,i in enumerate(list_add):

        print(j+1,".client",j+1,"address is-->",i)
  
    

    

def sending():
    '''
    while True:#group msging like whatsapp
        for h,i in enumerate(list_con):
            try:
                data=i.recv(1024).decode()
                print(data)
                for j in list_con:
                    if i!=j:
                        j.send(("msg from client"+h+" ->"+str(data)).encode())
            except Exception as e:
                pass
            '''
    while True:
        listing()
        x = int(input("enter your chooise-- "))
        list_con[x-1].send(input("enter msg----->").encode())
        data = list_con[x-1].recv(1024).decode()
        print("msg from client",x,"-->",str(data))

'''
def receving():
    while True:
        listing()

        for j,i in enumerate(list_con):
            try:
                data=i.recv(1024).decode()
                con1,client1=i,j
            except:
                pass
        print(data,"form client->",client1)
        for i in list_con:
            if i!=con1:
                i.send((data).encode())
'''

t1=threading.Thread(target=accepting)
t2=threading.Thread(target=sending)
t1.start()



    


