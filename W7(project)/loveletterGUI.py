import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
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
        self.resize(1200, 700)
        self.move(0, 0)
        self.setWindowIcon(
            QIcon(r"./img/pp2.png"))

        # 배경
        bg_img = QPixmap(r".\img\bgbg.png")
        self.bg = QLabel("bg", self)
        self.bg.resize(1200, 700)
        self.bg.setPixmap(bg_img)

        # player Label 만들기
        self.playerList = [QLabel("player{}".format(i+1), self)
                           for i in range(4)]
        [label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
         for label in self.playerList]
        self.playerList[0].setGeometry(286, 582, 80, 25)
        self.playerList[1].setGeometry(677, 453, 80, 25)
        self.playerList[2].setGeometry(568, 170, 80, 25)
        self.playerList[3].setGeometry(184, 205, 80, 25)
        # self.playerList[0].alignment()

        # 공격대상 버튼
        self.playerBtnList = [QPushButton(
            "Player{}".format(i+1), self) for i in range(4)]
        self.playerBtnList[0].setGeometry(286, 582, 80, 25)
        self.playerBtnList[1].setGeometry(677, 453, 80, 25)
        self.playerBtnList[2].setGeometry(568, 170, 80, 25)
        self.playerBtnList[3].setGeometry(184, 205, 80, 25)
        for i, btn in enumerate(self.playerBtnList):
            btn.setHidden(True)
            self.playerBtnEvent(btn, i)

# 1번 카드 선택시 선택할 카드 버튼
        self.selTypeBtnList = [QPushButton(
            "{}번".format(i+2), self) for i in range(7)]
        for i, btn in enumerate(self.selTypeBtnList):
            if i < (len(self.selTypeBtnList)//2)+1:
                btn.setGeometry(660+i*30, 540, 30, 40)
            else:
                btn.setGeometry(
                    645+(i-len(self.selTypeBtnList)//2)*30, 590, 30, 40)
            btn.setHidden(True)

            self.typeBtnEvent(btn, i)  # 선택된 카드를 서버로 보내기 위한 함수로 이동시킴

        # 하트 뱃지
        self.heart_img = QPixmap(
            r"./img/coin.png").scaled(28, 30)
        self.heartBadgeList = [[QLabel(self)
                                for i in range(3)] for j in range(4)]
        for Label in self.heartBadgeList:       # badge리스트에 있는 Label에
            for heart in Label:                 # 각 Label에
                heart.setPixmap(self.heart_img)  # 하트 이미지를 입혀
                heart.setHidden(True)           # 일단 숨겨놔
        for j in range(3):
            self.heartBadgeList[0][j].setGeometry(286+j*26, 550, 28, 30)  # 맨아래
            self.heartBadgeList[1][j].setGeometry(677+j*26, 479, 28, 30)  # 오른쪽
            self.heartBadgeList[2][j].setGeometry(568+j*26, 138, 28, 30)  # 위쪽
            self.heartBadgeList[3][j].setGeometry(184+j*26, 173, 28, 30)  # 왼쪽

        self.backImg = QPixmap(r".\img\0.jpg").scaled(
            78, 103, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.playerCardList = [[QLabel(self)
                                for i in range(2)] for j in range(4)]
        for player in self.playerCardList:
            for card in player:
                card.setPixmap(self.backImg)
                card.setHidden(True)
        self.playerCardList[0][0].move(378, 480)  # 자신의 1번카드 맨 아래
        self.playerCardList[0][1].move(488, 480)  # 자신의 2번카드
        self.playerCardList[1][0].move(678, 340)  # player3의 1번카드 오른쪽
        self.playerCardList[1][1].move(678, 230)  # player3의 2번카드
        self.playerCardList[2][0].move(478, 90)  # player2의 1번카드 맨 위
        self.playerCardList[2][1].move(388, 90)  # player2의 2번카드
        self.playerCardList[3][0].move(185, 240)  # player1의 1번카드 왼쪽
        self.playerCardList[3][1].move(185, 350)  # player1의 2번카드

        self.playerCardList[0][0].mousePressEvent = self.sendSelected1
        self.playerCardList[0][1].mousePressEvent = self.sendSelected2

        self.centerCardList = [QLabel(self) for i in range(16)]
        self.grave = [QLabel(self) for i in range(16)]
        for i in range(16):
            self.centerCardList[i].setPixmap(self.backImg)
            self.centerCardList[i].move(478+i*2, 270+i*2)
            self.grave[i].move(378+i*2, 270+i*2)
            self.grave[i].resize(78, 103)

        self.userName = QLineEdit(self)
        self.userName.setPlaceholderText("username")
        self.userName.setGeometry(927, 350, 110, 38)

        self.connectButton = QPushButton("연결", self)
        self.connectButton.setGeometry(1052, 350, 110, 38)
        self.connectButton.clicked.connect(self.connection)
        self.connectButton.setDefault(True)

        #start button
        self.startBtn = QPushButton("게임시작", self)
        self.startBtn.setGeometry(800, 350, 110, 38)
        self.startBtn.setHidden(True)
        self.startBtn.clicked.connect(self.startGame)

        # 채팅창
        self.main_text = QTextEdit(self)  # 메인 텍스트
        self.main_text.setReadOnly(True)
        self.main_text.setGeometry(800, 400, 361, 180)

        self.send_box = QLineEdit(self)  # 문자 입력창
        self.send_box.setGeometry(800, 590, 270, 40)
        # self.send_box.returnPressed.connect(self.sendData)

        self.send_button = QPushButton('보내기', self)  # 문자 보내기
        self.send_button.setGeometry(1082, 590, 80, 40)
        self.send_button.clicked.connect(self.sendData)

        dog = QPixmap(
            "./img/pp.png").scaled(100, 100)
        self.dog = QLabel(self)
        self.dog.setPixmap(dog)
        self.dog.move(1074, 498)

        # 네트워크 연결하기

        self.server_ip = '192.168.0.29'
        self.port_address = 5000

        self.socket = QtNetwork.QTcpSocket(self)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)

        # # Game Rule
        self.gamerule = QLabel("""
                              ※ 게임 방법 ※\n
 [1] 자신의 턴에 카드 2장이 주어집니다. 
 [2] 카드 한 장을 선택합니다.
 [3] 카드의 기능은 공격가능 대상에게만 사용할 수 있습니다.
 [4] 카드를 사용하면 자동으로 차례가 넘어갑니다.
 [5] 마지막 까지 카드를 들고 있는 사람이 승자가 됩니다.  
    *2인 이상 일 경우: 카드를 비교해서 숫자가 높은사람이 승!\t\n

                              ※ 게임 목표 ※\n
 1게임은 총 3판으로 구성되고,
 1판이 끝날 때 마다 승자는 초코비를 받게 됩니다. 
 먼저 초코비 3개를 모은 사람이 최종 승자가 됩니다.""", self)
        self.gamerule.move(800, 100)
        self.gamerule.setStyleSheet(
            "padding: 0px; margin:0px; font-family: 맑은 고딕; border-radius:10;")

        # # ChatBox
        self.show()

    def startGame(self):
        self.startBtn.setHidden(True)
        self.send("sys:start")

    def playerBtnEvent(self, btn, i):
        btn.clicked.connect(lambda: self.playerBtnEvent2(btn, i))

    def playerBtnEvent2(self, btn, i):
        self.send("sys:selectedPlayer:{}".format(i))
        for bt in self.playerBtnList:
            bt.setHidden(True)

    def typeBtnEvent(self, btn, i):
        btn.clicked.connect(lambda: self.typeBtnEvent2(btn, i))

    def typeBtnEvent2(self, btn, i):
        self.send("sys:selectedType:{}".format(i+2))
        for bt in self.selTypeBtnList:
            bt.setHidden(True)

    def sysPrint(self, list):
        for i, card in enumerate(self.centerCardList):
            if i < int(list[0]):
                card.setHidden(False)
            else:
                card.setHidden(True)
        for i, card in enumerate(self.grave):
            if i < len(eval(list[1])):
                card.setHidden(False)
                card.setPixmap(QPixmap(r".\img\{}.jpg".format(
                    eval(list[1])[i])).scaled(78, 103, Qt.KeepAspectRatio, Qt.FastTransformation))
            else:
                card.setHidden(True)
        for i, card in enumerate(self.playerCardList[0]):
            if i < len(eval(list[2])):
                card.setPixmap(QPixmap(r".\img\{}.jpg".format(
                    eval(list[2])[i])).scaled(100, 139, Qt.KeepAspectRatio, Qt.FastTransformation))
                card.setHidden(False)
                toolTipL = ["", "상대를 선택하고 카드를 추측하여 맞으면 상대가 탈락한다",
                            "상대를 선택하고 가진 카드 확인한다",
                            "상대를 선택하고 자신의 카드와 비교하여 낮은 숫자를 가진 사람이 탈락",
                            "다음 자신의 턴이 올 때까지 다른 카드의 공격을 받지 않는다",
                            "상대를 선택하고 카드를 버리고 다시 뽑는다",
                            "상대를 선택하고 카드를 교환한다",
                            "5번 또는 6번 카드를 가지고 있으면 반드시 버려진다",
                            "버리면 무조건 패배(버릴 수 없음)"]
                card.setToolTip(toolTipL[eval(list[2])[i]])
            else:
                card.setHidden(True)
        for i in range(len(list)-3):
            for card in self.playerCardList[i+1]:
                if len(list[i+3]) == 1:
                    if self.playerCardList[i+1].index(card) < int(list[i+3]):
                        card.setPixmap(QPixmap(r".\img\0.jpg").scaled(
                            78, 103, Qt.KeepAspectRatio, Qt.FastTransformation))
                        card.setHidden(False)
                    else:
                        card.setHidden(True)
                else:
                    self.playerCardList[i+1][0].setPixmap(QPixmap(r".\img\{}.jpg".format(
                        eval(list[i+3])[0])).scaled(78, 103, Qt.KeepAspectRatio, Qt.FastTransformation))

    def displayError(self, e):
        QMessageBox.information(self, "Connection", "서버가 연결을 해제했습니다.")

    def readData(self):
        global myTurn
        message = self.socket.readLine().data().decode("utf-8").split("/")
        print(message)
        for submessage in message:
            if submessage == "":
                continue
            elif submessage == "NICK":
                self.socket.write(self.userName.text().encode("utf-8"))
                self.userName.setReadOnly(True)
            elif submessage.split(":")[0] == "sys":
                msg = submessage.split(":")
                if msg[1] == "print":
                    self.sysPrint(msg[2:-1])
                elif msg[1] == "turn":
                    myTurn = True
                elif msg[1] == "reSelectCard":
                    QMessageBox.information(self, "reselect", "카드를 다시 선택하세요!")
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
                elif msg[1] == "youAreFirst":
                    self.startBtn.setHidden(False)
                elif msg[1] == "favorability":
                    for idx, cnt in enumerate(eval(msg[2])):
                        for i in range(cnt):
                            self.heartBadgeList[idx][i].setHidden(False)
                elif msg[1] == "winner":
                    mb = QMessageBox()
                    mb.setText("축하합니다!!!\n{}".format(msg[2]))
                    mb.setWindowTitle("winner message")
                    mb.setIconPixmap(QPixmap(r".\img\jg.jpg"))
                    mb.exec_()
            else:
                self.main_text.append(submessage)

    def sendSelected1(self, e):
        global myTurn
        if myTurn:
            self.send("sys:selectedCard:1")
            myTurn = False

    def sendSelected2(self, e):
        global myTurn
        if myTurn:
            self.send("sys:selectedCard:2")
            myTurn = False

    def send(self, message):
        self.socket.write(message.encode("utf-8"))

    def sendData(self, e):
        message = "{} : {}".format(self.userName.text(), self.send_box.text())
        if message.find("/") != -1:
            QMessageBox.information(self, "fail", "입력 불가능한 단어가 포함되어 있습니다.\n")
        else:
            self.send(message)
            self.send_box.clear()
            self.send_box.setFocus()

    def closeEvent(self, e):
        self.socket.disconnectFromHost()

    def connection(self, e):
        if self.userName.text() == "sys":
            QMessageBox.information(self, "fail", "사용 불가능한 닉네임 입니다.\n")
        else:
            self.socket.connectToHost(self.server_ip, self.port_address)
            if self.socket.waitForConnected(1000):
                self.connectButton.setEnabled(False)
                self.send_button.setDefault(True)
                self.send_box.setFocus()
                print("연결성공")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
