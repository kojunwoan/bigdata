import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtWidgets, QtNetwork

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    # def Turn(self,e):
    #     self.p1_card1.setPixmap(self.guard_1_img_100)
    
    
    # def TurnBack(self,e):
    #     self.p1_card1.setPixmap(self.back_img)

    def initUI(self):
        self.setWindowTitle("Love Letter♡")
        self.resize(1200,700)
        self.move(0,0)

        # 배경 
        # bg_img = QPixmap("./img/loveletter/bg3_1200.jpg")
        # self.bg = QLabel("bg",self)
        # self.bg.resize(1200,700)
        # self.bg.setPixmap(bg_img)
        

        # player Label 만들기
        self.playerList = [QLabel("player{}".format(i+1)) for i in range(4)]
        self.playerList[0].move(377,554)
        self.playerList[1].move(90,300)
        self.playerList[2].move(377,83)
        self.playerList[3].move(717,300)

        self.imgList = [[QPixmap(r"E:\dev\python_workspace\W7(project)\img\{}_78.jpg".format(i)) for i in range(9)],
                        [QPixmap(r"E:\dev\python_workspace\W7(project)\img\{}_100.jpg".format(i)) for i in range(9)]]

        self.playerCardList = [[QLabel(self) for i in range(2)] for j in range(4)]
        [[card.setPixmap(self.imgList[1][0]) if self.playerCardList.index(player) == 0 else card.setPixmap(self.imgList[0][0]) for card in player] for player in self.playerCardList]

        self.playerCardList[0][0].move(290,440)
        self.playerCardList[0][1].move(400,440)
        self.playerCardList[1][0].move(90,300)
        self.playerCardList[1][1].move(90,190)
        self.playerCardList[2][0].move(310,50)
        self.playerCardList[2][1].move(400,50)
        self.playerCardList[3][0].move(600,300)
        self.playerCardList[3][1].move(600,190)

        self.centerCardList = []
        for i in range(4):
            lb2 = QLabel(self)
            lb2.setPixmap(self.imgList[0][0])
            self.centerCardList.append(lb2)

        self.centerCardList[0].move(300,250)
        self.centerCardList[1].move(400,250)
        self.centerCardList[2].move(402,252)
        self.centerCardList[3].move(404,254)

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
        
        self.server_ip = '192.168.0.29'
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
        message = self.socket.readLine().data().decode("utf-8")
        if message == "NICK":
            self.socket.write(self.userName.text())
        else:
            self.main_text.append(message)

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

    def Turn(self, e):
        self.p1_card1.setPixmap(self.guard_1_img_100)

    def drawCard(self, e):
        self.p1_card1.move(300,440)
        self.p1_card2 = QLabel(self)        
        self.p1_card2.setPixmap(self.back_img_100)
        self.p1_card2.move(400,440)
        

        self.show()
        # # Game Rule
        # self.gamerule = QLabel("※ 게임 방법 ※\n1 경비병: 상대를 선택하고 카드를 추측하여 맞으면 탈락한다\n2 사제: 대상 선택 후 가진 카드 확인\n3 남작: 대상 선택 후 자신의 카드와 비교하여 낮은 숫자가 탈락\n4 시녀: 다음 턴이 올 때까지 다른 카드의 능력 무효화\n5 왕자: 카드를 버리고 다시 뽑는다\n6 왕: 대상을 선택하고 카드를 교환한다\n7 백작부인: 5번 또는 6번 카드를 가지고 있으면 반드시 버려진다\n8 공주: 버리면 무조건 패배(버릴 수 없음)",self)
        # self.gamerule.move(800,5)

        # # ChatBox
        




if __name__=="__main__":
    app = QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())
