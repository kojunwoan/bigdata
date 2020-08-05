from socket import *

ip = "192.168.0.37"
port = 5000

clientSock = socket(AF_INET,SOCK_STREAM)
# for i in range(100,65535):          #포트스캐닝
#     try:
#         clientSock.connect(("119.205.197.57",i))
#     except:
#         print(i,"는 안되")

clientSock.connect((ip,port))
print("접속완료!")
while True:
    clientSock.send(input(">>>").encode('utf-8'))
    print("서버가 보낸 메세지 :",clientSock.recv(1024).decode('utf-8'))