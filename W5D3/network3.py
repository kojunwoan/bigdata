#서버 사이드
from socket import *

port = 5000

serverSock =socket(AF_INET,SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(1)
print("%d번 포트로 접속 대기중"%port)

ConnectionSock, addr = serverSock.accept()

print(addr,"에서 접속되었습니다.")

while True:
    print("클라이언트가 보낸 메세지 :",ConnectionSock.recv(1024).decode("utf-8"))
    ConnectionSock.send(input(">>>").encode("utf-8"))