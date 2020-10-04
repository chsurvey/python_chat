from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1',8080))

msg = clientSock.recv(1024)
print(msg.decode('utf-8'))
