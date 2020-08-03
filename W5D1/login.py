import cx_Oracle
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def dbcheck(self):
        #1. connection 객체 생성
        connection = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
        #2. cursor 객체 생성
        cur = connection.cursor()
        #3. 사용할 sql문 객체
        sql = "select id from member where id = :id and pw = :pw"
        #4. 실행
        cur.execute(sql,id=self.leID.text(),pw=self.lePW.text())
        #5. 로직처리
        for id in cur:
            if id!=None:
                print("로그인성공")
                QMessageBox.question(self,"로그인 성공", "조선의 궁궐에 당도한 것을 환영하오, 낯선이여.", QMessageBox.Yes, QMessageBox.Yes)
        #6. 자원 반납
        connection.close()
    def login(self):
        pass
    def reg(self):
        pass
    def close(self):
        if QMessageBox.question(self, "메세지", "정말 나갈려구?", QMessageBox.Yes| QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            QCoreApplication.instance().quit()


    def initUI(self):
        #PyQt에서 이벤트(signal)처리할때 사용되는 함수를 이벤트 핸들러(slot)이라고 한다.
        
        back = QPixmap("./img/0803.jpg")
        img = QLabel("back",self)
        img.setPixmap(back)

        #라벨 2개
        self.labelID = QLabel("ID",self)
        self.labelPW = QLabel("PW",self)
        #폰트 크게
        font1 = self.labelID.font()
        font1.setPointSize(30)
        font1.setBold(True)
        self.labelID.setFont(font1)
        self.labelPW.setFont(font1)

        self.labelID.move(470,150)
        self.labelPW.move(470,230)

        self.labelID.resize(120,50)
        self.labelPW.resize(120,50)

        #QlineEdit
        self.leID = QLineEdit(self)
        self.lePW = QLineEdit(self)

        self.leID.move(550,150)
        self.lePW.move(550,230)
        self.leID.resize(120,50)
        self.lePW.resize(120,50)

        #푸쉬버튼 객체 생성
        self.btnlogin = QPushButton("헬조선 로그인",self)
        self.btnlogin.resize(120,50)
        self.btnlogin.move(550,330)
        self.btnlogin.clicked.connect(self.dbcheck)

        self.btnreg = QPushButton("헬조선 가입",self)
        self.btnreg.resize(120,50)
        self.btnreg.move(550,400)
        self.btnreg.clicked.connect(self.reg)

        btnclose = QPushButton("X",self)
        btnclose.resize(30,30)
        btnclose.move(660,10)
        # btnclose.clicked.connect(QCoreApplication.instance().quit)
        btnclose.clicked.connect(self.close)

        '''
        LayOut, BoxLayout, 수평상자 수직상자
        '''

        """
        hboxID = QHBoxLayout()
        hboxID.addStretch(1)
        hboxID.addWidget(self.labelID)
        hboxID.addWidget(self.leID)
        hboxID.addStretch(1)

        hboxPW = QHBoxLayout()
        hboxPW.addStretch(1)
        hboxPW.addWidget(self.labelPW)
        hboxPW.addWidget(self.lePW)
        hboxPW.addStretch(1)

        hboxbtn = QHBoxLayout()
        hboxbtn.addStretch(1)
        hboxbtn.addWidget(self.btn1)
        hboxbtn.addWidget(self.btn3)
        hboxbtn.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hboxID)
        vbox.addLayout(hboxPW)
        vbox.addLayout(hboxbtn)
        self.setLayout(vbox)
        """

        self.setWindowTitle("Welcome to Hell Chosun, stranger")
        self.move(0,0)
        self.setWindowIcon(QIcon('./img/exit.jpg'))
        self.resize(720,950)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())