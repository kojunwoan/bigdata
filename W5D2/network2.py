#클라이언트 사이트
from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.0.37',5000)) #서버랑 연결, 루프백 주소

clientSock.send(input().encode("utf-8"))

data = clientSock.recv(1024)
print("서버가 보낸 데이터 : ", data.decode("utf-8"))
print("연결 성공")
