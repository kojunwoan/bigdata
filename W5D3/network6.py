#클라이언트 사이드
from socket import *

ip = '192.168.0.37'
port = 5000

def send(sock):
    sock.send(input(">>>").encode("utf-8"))
def recive(sock):
    print("서버가 보낸 메세지 :",sock.recv(1024).decode('utf-8'))

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((ip,port))
print("접속완료")

while True:
    send(clientSocket)
    recive(clientSocket)