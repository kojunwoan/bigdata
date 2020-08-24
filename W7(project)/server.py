import socket
import threading
from card import Card
from user import User
from random import choice
import time

forXpeople = 2

def buildADeckOfCards():
    for ctype,item in enumerate(Cardinfo):
        for i in range(item.get("cnt")):
            CardL.append(Card(ctype+1,item.get("rank"),item.get("name"),item.get("img")))


Cardinfo = [{"rank" : 1,"name":"Guard Odette", "img":"1_guard.jpg","cnt" : 5},
        {"rank" : 2,"name":"Priest Tomas", "img":"2_priest.jpg","cnt" : 2},
        {"rank" : 3,"name":"Baron Talus", "img":"3_baron.jpg","cnt" : 2},
        {"rank" : 4,"name":"Handmaid Susannah", "img":"4_handmaid.jpg","cnt" : 2},
        {"rank" : 5,"name":"Prince Arnaud", "img":"5_prince.jpg","cnt" : 2},
        {"rank" : 6,"name":"King Arnaud IV", "img":"6_king.jpg","cnt" : 1},
        {"rank" : 7,"name":"Countess Wilhelmina", "img":"7_countess.jpg","cnt" : 1},
        {"rank" : 8,"name":"Princess Annette", "img":"8_princess.jpg","cnt" : 1}]

CardL = []
host = ""
port = 5000

# 서버 시작
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

gaming = True
selected = False
cmsg = ""
clients = []
grave = []
target = -1
targetT = -1

def broadcast(msg):
    for client in clients:
        client.connectionSock.send(msg)

def handle(client):
    global selected
    global cmsg
    global grave
    global clients
    global target
    global targetT
    while True:
        try:
            msg = client.connectionSock.recv(1024).decode('utf-8')
            print(msg)
            if msg[:3] == "sys":
                cmsg = msg.split(":")
                if cmsg[1] == "selectedCard":
                    if client.useCard(int(cmsg[2])-1):
                        grave.append([client.selectedCard,clients.index(client)])
                        for card in grave:
                            print(card[0].type, card[0].name)
                        if client.selectedCard.type in [4,7]:
                            selected = True
                            makeSysPrint()
                        else:
                            user = []
                            for cli in clients:
                                if cli.connectionSock == client.connectionSock and not client.selectedCard.type == 5:
                                    continue
                                if cli.isAlive and not cli.protected:
                                    idx = clients.index(cli) - clients.index(client)
                                    if idx < 0:
                                        idx += len(clients)
                                    user.append(idx,)
                            if len(user) == 0:
                                selected = True
                                makeSysPrint()
                            else:
                                makeSysPrint()
                                print("sys:selectPlayer:{}".format(user))
                                client.connectionSock.send("sys:selectPlayer:{}".format(user).encode('utf-8'))
                                time.sleep(0.2)
                    else:
                        client.connectionSock.send("sys:reSelectCard".encode("utf-8"))
                        # time.sleep(0.2)
                if cmsg[1] == "selectedPlayer":
                    target = clients[(int(cmsg[2])+clients.index(client))%len(clients)]
                    print(target)
                    if client.selectedCard.type == 1:
                        print("1번카드 사용")
                        client.connectionSock.send("sys:selectType".encode('utf-8'))
                        # time.sleep(0.2)
                    else:
                        selected = True
                if cmsg[1] == "selectedType":
                    targetT = int(cmsg[2])
                    selected = True
            else:
                broadcast(msg.encode('utf-8'))
        except: 
            nickname = client.nick
            client.connectionSock.close() 
            clients.remove(client) 
            broadcast("{}님 로그아웃".format(nickname).encode("utf-8"))
            break

def receive():
    global forXpeople
    while len(clients) < forXpeople:
        print("클라이언트 접속 중")
        connectionSock, addr = server.accept()
        print(str(addr)+"로부터 연결됨")

        connectionSock.send("NICK".encode("utf-8"))
        connectionSock.send("도시국가 템페스트에 오신 것을 환영합니다.".encode("utf-8"))
        nickname = connectionSock.recv(1024).decode("utf-8")
        clients.append(User(connectionSock,nickname))
       
        threading.Thread(target=handle, args=(clients[-1],)).start()

def makeSysPrint():
    global clients
    global grave
    submsg = ""
    for client in clients:
        submsg += str(len(client.prossessionCard))+":"
    for client in clients:
        graveCardType = [card.type for card,user in grave]
        clientCardType = [card.type for card in client.prossessionCard]
        msg = "sys:print:{}:{}:{}:{}".format(len(CardL),graveCardType,clientCardType,submsg[2:])
        client.connectionSock.send(msg.encode("utf-8"))                              
        submsg = submsg[2:]+submsg[:2]
    
def nickPrint():
    global clients
    nickL = [client.nick for client in clients]
    for client in clients:
        client.connectionSock.send("sys:nick:{}".format(nickL).encode("utf-8"))
        nickL.append(nickL[0])
        del nickL[0]

def giveCard(user):
    global CardL
    card = choice(CardL)
    user.takeCard(card)
    CardL.remove(card)

def game():
    global forXpeople
    global gaming
    global clients
    global cmsg
    global CardL
    global grave
    global selected
    global target
    global targetT
    while len(clients) == forXpeople:
        while gaming:
            CardL = []
            buildADeckOfCards()
            nickPrint()
            time.sleep(0.1)
            turn = 0
            grave = []
            card = choice(CardL)
            grave.append([card,-1])
            CardL.remove(card)
            print(grave[0][0].type, grave[0][0].name)
            for client in clients:
                giveCard(client)
                for card in CardL:
                    print(card.type, card.name)
            while len(CardL)>0:
                client = clients[turn%len(clients)]
                if client.isAlive:
                    client.protected = False
                    makeSysPrint()
                    time.sleep(0.2)
                    giveCard(client)
                    makeSysPrint()
                    time.sleep(0.2)
                    selected = False
                    print(client.prossessionCard[0].type)
                    print(client.prossessionCard[1].type)
                    msg = "sys:turn:{}:{}".format(client.prossessionCard[0].type,client.prossessionCard[1].type)
                    client.connectionSock.send(msg.encode("utf-8"))
                    while not selected:
                        time.sleep(0.2)
                    time.sleep(1)
                    note = ""
                    if client.selectedCard.type == 1:
                        grave,note = client.execute(target,grave,targetT)
                    elif client.selectedCard.type == 5:
                        grave,CardL,note = client.execute(target,grave,CardL)
                    elif client.selectedCard.type == 3:
                        grave,note = client.execute(target,grave)
                    elif client.selectedCard.type == 6:
                        note = client.execute(target)
                    else:
                        note = client.execute()
                    makeSysPrint()
                    time.sleep(0.2)
                    cntAlive = 0
                    for client in clients:
                        if client.isAlive:
                            cntAlive += 1
                    if cntAlive==1:
                        break
                turn += 1
            for client in clients:
                client.init()

        
receive()
game()