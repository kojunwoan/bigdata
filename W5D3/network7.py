#서버 사이드
from socket import *
from threading import *
from time import *

ip = ''
port=5000

def send(sock):
    while True:
        sock.send(input(">>>").encode("utf-8"))
def recive(sock):
    while True:
        print("클라이언트가 보낸 메세지 :",sock.recv(1024).decode('utf-8'))

serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind((ip,port))
serverSock.listen(1)
print("%d번 포트 접속 대기중.."%port)

ConnectionSock, addr = serverSock.accept()

print(addr,"에서 접속되었습니다.")

Thread(target=send,args=(ConnectionSock,)).start()
Thread(target=recive,args=(ConnectionSock,)).start()

while True:
    sleep(100000)