from socket import *

def send(Sock):
    msg=input(">>>")
    Sock.send(msg.encode('utf-8'))

def receive(Sock):
    msg = Sock.recv(1024)
    print(msg.decode('utf-8'))

port = 8080

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1',8080))

print("접속 성공")

while(True):
    receive(clientSock)

    send(clientSock)