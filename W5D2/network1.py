#서버 사이드
from socket import *
import random
d = ["안녕","왜끊냐","재미없다","너무하네","욕좀 그만해","욕쟁이 아줌마야","왜??","나도몰라","8갠데","10개네"]
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',5000))#port
print("사용자의 접속을 대기합니다.")
serverSock.listen(1)#연결을 기다림(수신.....)
connectionSock, addr = serverSock.accept()
print("연결성공")
while True:
    a = d[random.randint(0,9)]
    data = connectionSock.recv(1024)
    msg = data.decode("utf-8")
    print(msg)
    print(a)
    # connectionSock.send(input().encode("utf-8"))
    connectionSock.send(a.encode("utf-8"))