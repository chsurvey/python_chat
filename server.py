from socket import *
import threading
import time

def send(Sock):
    while(True):
        msg = input()
        Sock.send(msg.encode('utf-8'))

def receive(Sock):
    while(True):
        msg = Sock.recv(1024)
        print("클라이언트 : "+msg.decode('utf-8'))

port = 8080

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen()

print("%d번 포트 접속 시도중.."%(port))

connectionSock, addr=serverSock.accept()

print("접속 성공(%s)"%(str(addr)))

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while(True):
    time.sleep(1)
    pass