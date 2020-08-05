#클라이언트 사이드
from socket import *
from threading import *

ip = '192.168.0.68'
port = 5000
nickname = "qwerty"

clientSock = socket(AF_INET,SOCK_STREAM)
clientSock.connect((ip,port))
print("접속완료")

#서버에 닉네임 보내기
def receiver():
    while True:
        try:
            msg = clientSock.recv(1024).decode("utf-8")
            if msg == "NICK":
                clientSock.send(nickname.encode("utf-8"))
            else:
                print(msg)
        except:
            print("에러발생 연결끊음")
            clientSock.close()
            break

#서버에 메세지 보내기
def send():
    while True:
        clientSock.send("{}:{}".format(nickname,input()).encode('utf-8'))

Thread(target=receiver).start()
Thread(target=send).start()
