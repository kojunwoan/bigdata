import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtWidgets, QtNetwork
from PyQt5 import *
from card import Card
myTurn = False
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Love Letter♡")
        self.resize(1200,700)
        self.move(0,0)

        # 배경 
        bg_img = QPixmap(r"E:\dev\python_workspace\W7(project)\img\bg3_1200.jpg")
        self.bg = QLabel("bg",self)
        self.bg.resize(1200,700)
        self.bg.setPixmap(bg_img)
        
        # player Label 만들기
        self.playerList = [QLabel("player{}".format(i+1),self) for i in range(4)]
        self.playerList[0].setGeometry(355,400, 78,25)
        self.playerList[1].setGeometry(600,420, 78,25)
        self.playerList[2].setGeometry(355,160, 78,25)
        self.playerList[3].setGeometry(90, 420, 78,25)
        # self.playerList[0].alignment()

        # 공격대상 버튼
        self.playerBtnList = [QPushButton("Player{}".format(i+1), self) for i in range(4)]
        self.playerBtnList[0].setGeometry(355,400, 78,25)
        self.playerBtnList[1].setGeometry(600,420, 78,25)
        self.playerBtnList[2].setGeometry(355,160, 78,25)
        self.playerBtnList[3].setGeometry(90, 420, 78,25)
        for i,btn in enumerate(self.playerBtnList):
            btn.setHidden(True)
            self.playerBtnEvent(btn,i) 
        
        # 1번 카드 선택시 선택할 카드 버튼
        self.selTypeBtnList = [QPushButton("{}번".format(i+2), self) for i in range(7)]
        for i,btn in enumerate(self.selTypeBtnList):
            if i<len(self.selTypeBtnList)//2: 
                btn.setGeometry(640+i*30,470, 30,40)
            else:
                btn.setGeometry(625+(i-len(self.selTypeBtnList)//2)*30,540, 30,40)
            btn.setHidden(True)
            self.typeBtnEvent(btn,i)


        self.backImg = QPixmap(r"E:\dev\python_workspace\W7(project)\img\0.jpg").scaled(78,103,Qt.KeepAspectRatio, Qt.FastTransformation)
        self.playerCardList = [[QLabel(self) for i in range(2)] for j in range(4)]
        for player in self.playerCardList:
            for card in player:
                card.setPixmap(self.backImg)
                card.setHidden(True)
        self.playerCardList[0][0].move(290,440)
        self.playerCardList[0][1].move(400,440)
        self.playerCardList[1][0].move(600,300)
        self.playerCardList[1][1].move(600,190)
        self.playerCardList[2][0].move(400,50)
        self.playerCardList[2][1].move(310,50)
        self.playerCardList[3][0].move(90,190)
        self.playerCardList[3][1].move(90,300)

        self.playerCardList[0][0].mousePressEvent = self.sendSelected1
        self.playerCardList[0][1].mousePressEvent = self.sendSelected2
        
        self.centerCardList = [QLabel(self) for i in range(16)]
        self.grave = [QLabel(self) for i in range(16)]
        for i in range(16):
            self.centerCardList[i].setPixmap(self.backImg)
            self.centerCardList[i].move(400+i*2,250+i*2)
            self.grave[i].move(300+i*2,250+i*2)
            self.grave[i].resize(78,103)
        
        # 채팅창
        self.main_text = QTextEdit(self) # 메인 텍스트
        self.main_text.setReadOnly(True)
        self.main_text.setGeometry(800,260,370,250)

        self.send_box = QLineEdit(self) # 문자 입력창
        self.send_box.setGeometry(800,540,290,40)
        # self.send_box.returnPressed.connect(self.sendData)

        self.send_button = QPushButton('send',self)  # 문자 보내기
        self.send_button.setGeometry(1100,540,70,40)
        self.send_button.clicked.connect(self.sendData)

        # 네트워크 연결하기 
        self.userName = QLineEdit(self)
        self.userName.setPlaceholderText("username")
        self.userName.setGeometry(800,190,80,35)
        
        self.server_ip = '192.168.0.29'
        self.port_address = 5000

        self.connectButton = QPushButton("Connect",self)
        self.connectButton.setGeometry(1080,190,90,35)
        self.connectButton.clicked.connect(self.connection)
        self.connectButton.setDefault(True)

        self.socket = QtNetwork.QTcpSocket(self)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)
        
        # # Game Rule
        self.gamerule = QLabel("""※ 게임 방법 ※
        1 경비병: 상대를 선택하고 카드를 추측하여 맞으면 탈락한다
        2 사제: 대상 선택 후 가진 카드 확인
        3 남작: 대상 선택 후 자신의 카드와 비교하여 낮은 숫자가 탈락
        4 시녀: 다음 턴이 올 때까지 다른 카드의 능력 무효화
        5 왕자: 카드를 버리고 다시 뽑는다
        6 왕: 대상을 선택하고 카드를 교환한다
        7 백작부인: 5번 또는 6번 카드를 가지고 있으면 반드시 버려진다
        8 공주: 버리면 무조건 패배(버릴 수 없음)""",self)
        self.gamerule.move(800,30)

        # # ChatBox
        self.show()

    def playerBtnEvent(self, btn, i):
        btn.clicked.connect(lambda : self.playerBtnEvent2(btn,i))

    def playerBtnEvent2(self, btn, i):
        self.send("sys:selectedPlayer:{}".format(i))
        for bt in self.playerBtnList:
            bt.setHidden(True)

    def typeBtnEvent(self, btn, i):
        btn.clicked.connect(lambda: self.typeBtnEvent2(btn,i)) 

    def typeBtnEvent2(self, btn, i):
        self.send("sys:selectedType:{}".format(i+2))
        for bt in self.selTypeBtnList:
            bt.setHidden(True)

    def sysPrint(self,list):
        for i,card in enumerate(self.centerCardList):
            if i < int(list[0]):
                card.setHidden(False)
            else:
                card.setHidden(True)
        for i,card in enumerate(self.grave):
            if i == 0:
                card.setPixmap(self.backImg)
            elif i < len(eval(list[1])):
                card.setHidden(False)
                card.setPixmap(QPixmap(r"E:\dev\python_workspace\W7(project)\img/"+str(eval(list[1])[i])+".jpg").scaled(78,103,Qt.KeepAspectRatio, Qt.FastTransformation))
            else:
                card.setHidden(True)
        for i,card in enumerate(self.playerCardList[0]):
            if i < len(eval(list[2])):
                self.playerCardList[0][i].setPixmap(QPixmap(r"E:\dev\python_workspace\W7(project)\img\{}.jpg".format(eval(list[2])[i])).scaled(100,139,Qt.KeepAspectRatio, Qt.FastTransformation))
                self.playerCardList[0][i].setHidden(False)
            else :
                card.setHidden(True)
        for i in range(len(list)-3):
            for card in self.playerCardList[i+1]:
                if self.playerCardList[i+1].index(card) < int(list[2+i+1]):
                    card.setHidden(False)
                else:
                    card.setHidden(True)

    def displayError(self, e):
        QMessageBox.information(self, "Connection", "서버가 연결을 해제했습니다.")

    def readData(self):
        global myTurn
        message = self.socket.readLine().data().decode("utf-8")
        print(message)
        if message == "NICK":
            self.socket.write(self.userName.text().encode("utf-8"))
            self.userName.setReadOnly(True)
        elif message.split(":")[0] == "sys":
            msg = message.split(":")
            print(msg)
            if msg[1] == "print":
                self.sysPrint(msg[2:-1])
            elif msg[1] == "turn":
                myTurn = True
            elif msg[1] == "reSelectCard":
                myTurn = True
            elif msg[1] == "selectPlayer":
                for idx in eval(msg[2]):
                    self.playerBtnList[idx].setHidden(False)
            elif msg[1] == "selectType":
                for btn in self.selTypeBtnList:
                    btn.setHidden(False)
            elif msg[1] == "nick":
                for i in range(len(self.playerList)):
                    if i < len(eval(msg[2])):
                        self.playerList[i].setText(eval(msg[2])[i])
                        self.playerBtnList[i].setText(eval(msg[2])[i])
                    else:
                        self.playerList[i].setHidden(True)
                        self.playerBtnList[i].setHidden(True)
            elif msg[1] == "notice":
                pass
            elif msg[1] == "D_notice":
                pass
            print("시스템 메세지 입니다.")
        else:
            self.main_text.append(message)
    
    def sendSelected1(self,e):
        global myTurn
        if myTurn:
            self.send("sys:selectedCard:1")
            myTurn = False

    def sendSelected2(self,e):
        global myTurn
        if myTurn:
            self.send("sys:selectedCard:2")
            myTurn = False

    def send(self, message):
        self.socket.write(message.encode("utf-8"))

    def sendData(self, e):
        message = "{} : {}".format(self.userName.text(),self.send_box.text())
        self.send(message)
        self.send_box.clear()
        self.send_box.setFocus()

    def closeEvent(self, e):
        self.socket.disconnectFromHost()
    
    def connection(self, e):
        self.socket.connectToHost(self.server_ip, self.port_address)
        if self.socket.waitForConnected(1000):
            self.user = self.userName.text()
            self.send(self.user)
            self.connectButton.setEnabled(False)
            self.send_button.setDefault(True)
            self.send_box.setFocus()
            print("연결성공")



if __name__=="__main__":
    app = QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())