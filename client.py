import socket
import threading
import time

def send(Sock):
    msg=input(">>>")
    Sock.send(msg.encode('utf-8'))

def receive(Sock):
    msg = Sock.recv(1024)
    print(msg.decode('utf-8'))

port = 8080

clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(('127.0.0.1',8080))

print("접속 성공")

sender = threading.Thread(target=sender, args=(clientSock, ))
receiver = threading.Thread(target=receive, args=(clientSock, ))


while(True):
    time.sleep(1)
    pass