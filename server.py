from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen()

connectionSock, addr=serverSock.accept()

msg=input("보낼 메시지 입력:")

connectionSock.send(msg.encode('utf-8'))
print("전송완료")
