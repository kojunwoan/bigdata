#브로드캐스트 이용 멀티채팅
from socket import *
from threading import *

host = ""
port = 5000

server = socket(AF_INET,SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []

#접속중인 모든 사용자들에게 메세지 전달
def broadcast(msg):
    for client in clients:
        client.send(msg)

#클라이언트의 메세지 처리하는 함수
def handler(client):
    while True:
        try:
            #클라이언트 메세지 수신
            msg = client.recv(1024)
            #브로드캐스트
            broadcast(msg)
            #화면에 출력
            print(msg.decode('utf-8'))
        except:
            #제거하고 클라이언트 닫기
            index = clients.index(client)
            #예외 발생한 클라이언트만 리스트에서 제거
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{}떠남!!".format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        connectionSock, addr = server.accept()
        print(addr,"로부터 연결")
        clients.append(connectionSock)
        
        #nickname 요청하기
        connectionSock.send("NICK".encode('utf-8'))
        nickname = connectionSock.recv(1024).decode('utf-8')
        nicknames.append(nickname)

        #접속자 소개해주기
        connectionSock.send("서버에 접속되었습니다. 환영합니다.".encode('utf-8'))
        broadcast("{}님이 접속하셔습니다.".format(nickname).encode('utf-8'))

        #핸들링 함수를 쓰레드
        Thread(target=handler,args=(connectionSock,)).start()

Thread(target=receive).start()