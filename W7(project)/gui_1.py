import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtWidgets, QtNetwork

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Love Letter♡")
        self.resize(1200,640)
        self.move(0,0)

        # 배경 
        bg_img = QPixmap("./img/loveletter/bg3_1200.jpg")
        self.bg = QLabel("bg",self)
        self.bg.resize(1200,640)
        self.bg.setPixmap(bg_img)
        

        # player Label 만들기
        self.playerList = [QLabel("player{}".format(i+1)) for i in range(4)]
        self.playerList[0].move(370,599)
        self.playerList[1].move(10,295)
        self.playerList[2].move(370,16)
        self.playerList[3].move(717,295)

        # cardList 만들기
        cardList = []
        
        guard_1 = '1'
        priest_2 = '2'
        baron_3 = '3'
        handmaid_4 = '4'
        prince_5 = '5'
        king_6 = '6'
        countess_7 = '7'
        princess_8 = '8'
        
        for i in range(5):
            cardList.append(guard_1)
        for j in range(2):
            cardList.append(priest_2)
            cardList.append(baron_3)
            cardList.append(handmaid_4)
            cardList.append(prince_5)
        cardList.append(king_6)
        cardList.append(countess_7)
        cardList.append(princess_8)

        # card이미지 Pixmap으로 객체생성
        self.guard_1_img = QPixmap("./img/loveletter/_78_1.jpg")
        self.priest_2_img = QPixmap("./img/loveletter/78_2.jpg")
        self.baron_3_img = QPixmap("./img/loveletter/_78_3.jpg")
        self.handmaid_4_img = QPixmap("./img/loveletter/_78_4.jpg")
        self.prince_5_img = QPixmap("./img/loveletter/_78_5.jpg")
        self.king_6_img = QPixmap("./img/loveletter/_78_6jpg")
        self.countess_7_img = QPixmap("./img/loveletter/_78_7.jpg")
        self.princess_8_img = QPixmap("./img/loveletter/_78_8.jpg")
        self.back_img = QPixmap("./img/loveletter/_78_0.jpg")

        self.c1 = QPixmap("./img/loveletter/1.jpg")
        self.c2 = QPixmap("./img/loveletter/2.jpg")
        self.c3 = QPixmap("./img/loveletter/3.jpg")
        self.c4 = QPixmap("./img/loveletter/4.jpg")
        self.c5 = QPixmap("./img/loveletter/5.jpg")
        self.c6 = QPixmap("./img/loveletter/6.g")
        self.c7 = QPixmap("./img/loveletter/7.jpg")
        self.c8 = QPixmap("./img/loveletter/8.jpg")
        self.c0 = QPixmap("./img/loveletter/0.jpg")
        
        # card Label 만들기
        # player1 card positioning
        self.p1_card1 = QLabel(self)
        self.p1_card1.setPixmap(self.c1)
        self.p1_card1.move(280,440)
        self.p1_card1.mousePressEvent = self.submitCard

        self.p1_card2 = QLabel(self)      
        # self.p1_card2.setPixmap(self.back_img_100)  
        # self.p1_card2.move(400,440)
        # '---------------------------'
        # player2 card positioning
        self.p2_card1 = QLabel(self)
        self.p2_card1.setPixmap(self.back_img)
        self.p2_card1.move(90,250)

        # self.p2_card2 = QLabel(self)        
        # self.p2_card2.setPixmap(self.back_img)
        # self.p2_card2.move(90,190)
        '---------------------------'
        # player3 card positioning
        self.p3_card1 = QLabel(self)
        self.p3_card1.setPixmap(self.back_img)
        self.p3_card1.move(350,50)

        # self.p3_card2 = QLabel(self)        
        # self.p3_card2.setPixmap(self.back_img)
        # self.p3_card2.move(400,50)
        '---------------------------'
        # player4 card positioning
        self.p4_card1 = QLabel(self)
        self.p4_card1.setPixmap(self.back_img)
        self.p4_card1.move(600,250)

        # self.p4_card2 = QLabel(self)        
        # self.p4_card2.setPixmap(self.back_img)
        # self.p4_card2.move(600,190)

        # center card positioning
        self.ccard1 = QLabel(self)
        self.ccard1.setPixmap(self.back_img)
        self.ccard1.move(300,250)

        self.card_deck1 = QLabel(self)
        self.card_deck1.setPixmap(self.back_img)
        self.card_deck1.move(400,250)
        self.card_deck2 = QLabel(self)
        self.card_deck2.setPixmap(self.back_img)
        self.card_deck2.move(402,252)

        self.card_deck3 = QLabel(self)
        self.card_deck3.setPixmap(self.back_img)
        self.card_deck3.move(404,254)
        self.card_deck3.mousePressEvent = self.drawCard

        # Game Rule
        self.gamerule = QLabel("※ 게임 방법 ※\n1 경비병: 상대를 선택하고 카드를 추측하여 맞으면 탈락한다\n2 사제: 대상 선택 후 가진 카드 확인\n3 남작: 대상 선택 후 자신의 카드와 비교하여 낮은 숫자가 탈락\n4 시녀: 다음 턴이 올 때까지 다른 카드의 능력 무효화\n5 왕자: 카드를 버리고 다시 뽑는다\n6 왕: 대상을 선택하고 카드를 교환한다\n7 백작부인: 5번 또는 6번 카드를 가지고 있으면 반드시 버려진다\n8 공주: 버리면 무조건 패배(버릴 수 없음)",self)
        self.gamerule.move(800,35)

        # 채팅창
        self.main_text = QTextEdit(self) # 메인 텍스트
        self.main_text.setReadOnly(True)
        self.main_text.setGeometry(800,260,370,250)

        self.send_box = QLineEdit(self) # 문자 입력창
        self.send_box.setGeometry(800,540,290,40)

        self.send_button = QPushButton('send',self)  # 문자 보내기
        self.send_button.setGeometry(1100,540,70,40)
        self.send_button.clicked.connect(self.sendData)

        # 네트워크 연결하기 
        self.userName = QLineEdit(self)
        self.userName.setPlaceholderText("username")
        self.userName.setGeometry(800,190,80,35)
        
        self.server_ip = '192.168.0.31'
        self.port_address = 5000

        self.connectButton = QPushButton("Connect",self)
        self.connectButton.setGeometry(1080,190,90,35)
        self.connectButton.clicked.connect(self.connection)
        self.connectButton.setDefault(True)

        self.socket = QtNetwork.QTcpSocket(self)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)
        
        self.show()
        
    def displayError(self, e):
        QMessageBox.information(self, "Connection", "서버가 연결을 해제했습니다.")

    def readData(self):
        self.message = self.socket.readLine().data().decode("utf-8")
        msg = self.message.split(":")
        if self.message == "NICK":
            self.socket.write(self.userName.text())

        if msg[0] == "sys":
            print("시스템 메세지 입니다.")

        else:
            self.main_text.append(self.message)

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
        self.userName.setReadOnly(True)
        self.socket.connectToHost(self.server_ip, self.port_address)
        if self.socket.waitForConnected(1000):
            self.user = self.userName.text()
            self.send("login %s" % self.user)
            self.connectButton.setEnabled(False)
            self.send_button.setDefault(True)
            self.send_box.setFocus()
            print("연결성공")

    def drawCard(self, e):
        self.p1_card2.setPixmap(self.c2)
        self.p1_card2.resize(100,138)   #카드 뽑으면 사이즈 조정
        self.p1_card2.move(400,440)     #카드 위치 주기 

    def submitCard(self, e):
        selectedCard = self.guard_1_img
        self.ccard1.setPixmap(selectedCard)
        self.p1_card1.clear()
        
        #if문으로 카드마다 다른 이벤트 주기
        if selectedCard == self.guard_1_img: #선택된 카드가 1번이면,
            self.ccard1.mousePressEvent = self.selectOpponent
        if selectedCard == self.priest_2_img: #선택된 카드가 2번이면,
            self.ccard1.mousePressEvent = self.selectOpponent
        if selectedCard == self.baron_3_img: #선택된 카드가 3번이면,
            self.ccard1.mousePressEvent = self.selectOpponent


    def selectOpponent(self,e):
        qmb = QMessageBox()
        qmb.setText("공격대상을 선택하세요!")
        qmb.addButton('1번', QMessageBox.YesRole)   # 호출번호 0 튜플로 가져옴
        qmb.addButton('2번', QMessageBox.YesRole)   # 호출번호 1
        qmb.addButton('3번', QMessageBox.YesRole)   # 호출번호 2
        response = qmb.exec_()
        print(response)


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())
