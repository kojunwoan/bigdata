import socket
import threading
from card import Card
from user import User
from random import randint

def buildADeckOfCards():
    for ctype,item in enumerate(Cardinfo):
        for i in range(item.get("cnt")):
            CardL.append(Card(ctype+1,item.get("rank"),item.get("name"),item.get("img")))
    for i in range(100):
        a = randint(0,len(CardL)-1)
        b = randint(0,len(CardL)-1)
        CardL[a], CardL[b] = CardL[b], CardL[a]  


Cardinfo = [{"rank" : 1,"name":"Guard Odette", "img":"1_guard.jpg","cnt" : 5},
        {"rank" : 2,"name":"Priest Tomas", "img":"2_priest.jpg","cnt" : 2},
        {"rank" : 3,"name":"Baron Talus", "img":"3_baron.jpg","cnt" : 2},
        {"rank" : 4,"name":"Handmaid Susannah", "img":"4_handmaid.jpg","cnt" : 2},
        {"rank" : 5,"name":"Prince Arnaud", "img":"5_prince.jpg","cnt" : 2},
        {"rank" : 6,"name":"King Arnaud IV", "img":"6_king.jpg","cnt" : 1},
        {"rank" : 7,"name":"Countess Wilhelmina", "img":"7_countess.jpg","cnt" : 1},
        {"rank" : 8,"name":"Princess Annette", "img":"8_princess.jpg","cnt" : 1}]

CardL = []

buildADeckOfCards()

host = ""
port = 5000

# 서버 시작
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

gaming = True
clients = []

def broadcast(msg):
    for client in clients:
        client.connectionSock.send(msg)

def handle(client):
    while True:
        try:
            msg = client.connectionSock.recv(1024)
            broadcast(msg)
            print(msg.decode("utf-8")) 
        except: 
            nickname = client.nick
            client.connectionSock.close() 
            clients.remove(client) 
            broadcast("{}님 로그아웃".format(nickname).encode("utf-8"))
            break

def receive():
    while len(clients) < 2:
        print("클라이언트 접속 중")
        connectionSock, addr = server.accept()
        print(str(addr)+"로부터 연결됨")

        connectionSock.send("NICK".encode("utf-8"))
        connectionSock.send("도시국가 템페스트에 오신 것을 환영합니다.".encode("utf-8"))
        nickname = connectionSock.recv(1024).decode("utf-8")
        clients.append(User(connectionSock,nickname))
       
        threading.Thread(target=handle, args=(clients[-1],)).start()

def game():
    global gaming
    while gaming:
        for client in clients:
            client.prossessionCard.append(CardL[1])
            del CardL[1]
        while len(CardL)
        if clients[0].isAlive:
            clients[0].isTurn = True
            clients[0].prossessionCard.append(CardL[1])

        gaming = False
        
receive()
game()


