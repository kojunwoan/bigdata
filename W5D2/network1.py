from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',5000))#port
print("사용자의 접속을 대기합니다.")
serverSock.listen(1)#연결을 기다림(수신.....)
connectionSock, addr = serverSock.accept()
print("연결성공")