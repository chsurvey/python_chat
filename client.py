from socket import *
import threading
import time

def send(Sock):
    while(True):
        msg=input()
        Sock.send(msg.encode('utf-8'))

def receive(Sock):
    while(True):
        msg = Sock.recv(1024)
        print("서버 : "+msg.decode('utf-8'))

port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1',port))

print("접속 성공")

sender = threading.Thread(target=send, args=(clientSock, ))
receiver = threading.Thread(target=receive, args=(clientSock, ))

sender.start()
receiver.start()

while(True):
    time.sleep(1)
    pass