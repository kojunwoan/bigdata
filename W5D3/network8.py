#클라이언트 사이드
from socket import *
from threading import *
from time import *

ip = '192.168.0.68'
port = 5000

def send(sock):
    while True:
        sock.send(input(">>>").encode("utf-8"))
def recive(sock):
    while True:
        print("서버가 보낸 메세지 :",sock.recv(1024).decode('utf-8'))

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((ip,port))
print("접속완료")

Thread(target=send,args=(clientSocket,)).start()
Thread(target=recive,args=(clientSocket,)).start()


while True:
    sleep(100000)