#서버 사이드
from socket import *
port=5000

def send(sock):
    sock.send(input(">>>").encode("utf-8"))
def recive(sock):
    print("클라이언트가 보낸 메세지 :",sock.recv(1024).decode('utf-8'))

serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(1)
print("%d번 포트 접속 대기중.."%port)

ConnectionSock, addr = serverSock.accept()

print(addr,"에서 접속되었습니다.")

while True:
    recive(ConnectionSock)
    send(ConnectionSock)