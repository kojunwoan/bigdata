import socket
import threading
from card import Card
from user import User
from random import choice
import time



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
target = None
targetT = None
ending = True

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
    global ending
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
                                client.connectionSock.send("sys:selectPlayer:{}/".format(user).encode('utf-8'))
                    else:
                        client.connectionSock.send("sys:reSelectCard/카드가 선택될 수 없습니다.".encode("utf-8"))
                elif cmsg[1] == "selectedPlayer":
                    target = clients[(int(cmsg[2])+clients.index(client))%len(clients)]
                    print(target)
                    if client.selectedCard.type == 1:
                        print("1번카드 사용")
                        client.connectionSock.send("sys:selectType/".encode('utf-8'))
                        # time.sleep(0.2)
                    else:
                        selected = True
                elif cmsg[1] == "selectedType":
                    targetT = int(cmsg[2])
                    selected = True
                elif cmsg[1] == "start":
                    print("스타트하래")
                    ending = False
            else:
                broadcast(msg.encode('utf-8'))
        except: 
            nickname = client.nick
            client.connectionSock.close() 
            clients.remove(client) 
            broadcast("{}님 로그아웃".format(nickname).encode("utf-8"))
            break

def receive():
    global ending
    while (len(clients) < 4) and ending:
        print("클라이언트 접속 중")
        connectionSock, addr = server.accept()
        if not ending:
            connectionSock.close()
        print(str(addr)+"로부터 연결됨")
        connectionSock.send("NICK/".encode("utf-8"))
        print("nick")
        nickname = connectionSock.recv(1024).decode("utf-8")
        connectionSock.send("떡잎마을에 오신 것을 환영합니다./".encode("utf-8"))
        clients.append(User(connectionSock,nickname))
        broadcast("{}님이 들어오셨습니다./".format(nickname).encode('utf-8'))
        threading.Thread(target=handle, args=(clients[-1],)).start()
        if len(clients) == 2:
            clients[0].connectionSock.send("sys:youAreFirst/".encode("utf-8")) 

def makeSysPrint():
    global clients
    global grave
    submsg = ""
    for client in clients:
        submsg += str(len(client.prossessionCard))+":"
    graveCardType = [0 if len(clients) == 2 and idx < 3 and user == -1 or idx < 1 and user == -1 else card.type for idx,[card,user] in enumerate(grave)]
    for client in clients:
        clientCardType = [card.type for card in client.prossessionCard]
        msg = "sys:print:{}:{}:{}:{}/".format(len(CardL),graveCardType,clientCardType,submsg[2:])
        client.connectionSock.send(msg.encode("utf-8"))                              
        submsg = submsg[2:]+submsg[:2]
    
def makeSysPrintTarget(player1, player2):
    global clients
    submsg = ""
    for client in clients:
        if client in [player1,player2]:
            submsg += str([client.prossessionCard[0].type]) + ":"
        else:
            submsg += str(len(client.prossessionCard)) + ":"
    graveCardType = [0 if len(clients) == 2 and idx < 3 and user == -1 or idx < 1 and user == -1 else card.type for idx,[card,user] in enumerate(grave)]
    for client in clients:
        if client == player1:
            msg = "sys:print:{}:{}:{}/".format(len(CardL),graveCardType,submsg)
            client.connectionSock.send(msg.encode("utf-8"))                     
        if len(submsg.split(":")[0]) == 1:
            submsg = submsg[2:]+submsg[:2]
        else:
            submsg = submsg[4:]+submsg[:4]

#호감도 토큰의 개수 전달   
def printFavorability():
    global clients
    cliFav = [client.favorability for client in clients]
    for client in clients:
        msg = "sys:favorability:{}/".format(cliFav)
        client.connectionSock.send(msg.encode("utf-8"))                              
        cliFav.append(cliFav[0])
        del cliFav[0]

def nickPrint():
    global clients
    nickL = [client.nick for client in clients]
    for client in clients:
        client.connectionSock.send("sys:nick:{}/".format(nickL).encode("utf-8"))
        nickL.append(nickL[0])
        del nickL[0]

def giveCard(user):
    global CardL
    card = choice(CardL)
    user.takeCard(card)
    CardL.remove(card)

def game(numCl):
    global gaming
    global clients
    global cmsg
    global CardL
    global grave
    global selected
    global target
    global targetT
    global ending
    first = 0
    while len(clients) == numCl:
        while gaming:
            CardL = []
            CardL = [Card(ctype+1,item.get("rank"),item.get("name"),item.get("img")) for ctype,item in enumerate(Cardinfo) for i in range(item.get("cnt"))]
            nickPrint()
            time.sleep(0.1)
            turn = 0
            grave = []
            if len(clients) == 2:
                for i in range(3):
                    card = choice(CardL)
                    grave.append([card,-1])
                    CardL.remove(card)
            else:
                card = choice(CardL)
                grave.append([card,-1])
                CardL.remove(card)
            print(grave[0][0].type, grave[0][0].name)
            for client in clients:
                giveCard(client)
                for card in CardL:
                    print(card.type, card.name)
            while len(CardL)>0:
                target = None
                client = clients[(first+turn)%len(clients)]
                if client.isAlive:
                    client.protected = False
                    makeSysPrint()
                    time.sleep(0.2)
                    giveCard(client)
                    makeSysPrint()
                    time.sleep(0.2)
                    selected = False
                    client.connectionSock.send("sys:turn/".encode("utf-8"))
                    while not selected:
                        time.sleep(0.2)
                    time.sleep(1)
                    if client.selectedCard.type == 2:
                        makeSysPrintTarget(client, target)
                    if client.selectedCard.type == 3:
                        makeSysPrintTarget(client, target)
                        makeSysPrintTarget(target, client)
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
                    elif client.selectedCard.type == 2:
                        note = client.execute(target)
                    else:
                        note = client.execute()
                    note += "/"
                    makeSysPrint()
                    time.sleep(0.2)
                    broadcast(note.encode('utf-8'))
                    time.sleep(0.2)
                    cntAlive = 0 
                    for client in clients:
                        if client.isAlive:
                            cntAlive += 1
                    if cntAlive==1:
                        for client in clients:
                            if client.isAlive:
                                first = clients.index(client)
                        break
                turn += 1
                if len(CardL) == 0:
                    clientCardType = [cli.prossessionCard[0].type if cli.isAlive else -1 for cli in clients]
                    if clientCardType.count(max(clientCardType)) == 1:
                        first = clientCardType.index(max(clientCardType))
                    else:
                        sumRank = [0 for i in clients]
                        for card,cli in grave:
                            if cli != -1:
                                sumRank[cli] += card.rank
                        for idx,cli in enumerate(clients):
                            if not cli.isAlive:
                                sumRank[idx] = 0
                        first = sumRank.index(max(sumRank))
            ending = True
            clients[first].connectionSock.send("sys:youAreFirst/".encode("utf-8")) 
            broadcast("{}님이 승리하셨습니다./".format(clients[first].nick).encode("utf-8"))
            clients[first].favorability += 1
            printFavorability()
            for client in clients:
                if client.favorability == 3:
                    broadcast("sys:winner:{}님이 최종승리하셨습니다./".format(client.nick).encode("utf-8"))
                    while ending:
                        time.sleep(0.2)
                    for cli in clients:
                        cli.favorability = 0
                    printFavorability()
            while ending:
                time.sleep(0.2)
            for client in clients:
                client.init()


threading.Thread(target=receive).start()
while ending:
    time.sleep(0.2)
print("게임 시작")
game(len(clients))