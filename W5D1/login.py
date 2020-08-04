import cx_Oracle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
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

        self.labelID.setGeometry(470,150,120,50)
        self.labelPW.setGeometry(470,230,120,50)

        #QlineEdit
        self.leID = QLineEdit(self)
        self.lePW = QLineEdit(self)

        self.leID.setGeometry(550,150,120,50)
        self.lePW.setGeometry(550,230,120,50)

        #푸쉬버튼 객체 생성
        self.btnlogin = QPushButton("헬조선 로그인",self)
        self.btnlogin.setGeometry(550,330,120,50)
        self.btnlogin.clicked.connect(self.dbcheck)

        self.btnreg = QPushButton("헬조선 가입",self)
        self.btnreg.setGeometry(550,400,120,50)
        self.btnreg.clicked.connect(self.register)
        
        self.btnreg2 = QPushButton("헬조선 가입2",self)
        self.btnreg2.setGeometry(550,450,120,50)
        self.btnreg2.clicked.connect(self.register2)

        btnclose = QPushButton("X",self)
        btnclose.setGeometry(660,10,30,30)
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
        self.setWindowIcon(QIcon('./img/exit.jpg'))
        self.setGeometry(0,0,720,950)
        self.show()


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
    def register(self):
        self.nw = MyRegisterWindow(self)
        self.nw.show()
    def register2(self):
        self.nw = MyRegisterWindow2(self)
        self.nw.show()

    def close(self):
        if QMessageBox.question(self, "메세지", "정말 나갈려구?", QMessageBox.Yes| QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            QCoreApplication.instance().quit()

class MyRegisterWindow(QMainWindow):
    def __init__(self,parent):
        super().__init__(parent)
        self.setWindowTitle("헬조선 가입")
        self.setGeometry(100,100,350,300)
        self.lbrgID = QLabel("ID",self)
        self.lbrgPW = QLabel("PW",self)
        self.lbrgNa = QLabel("Name",self)

        self.lergID = QLineEdit(self)
        self.lergPW = QLineEdit(self)
        self.lergNa = QLineEdit(self)

        self.submit = QPushButton("가입하기",self)
        self.submit.clicked.connect(self.regdit)

# setGeometry로 해보자
        self.lbrgID.setGeometry(50,50,50,30)
        self.lbrgPW.setGeometry(50,100,50,30)
        self.lbrgNa.setGeometry(50,150,50,30)

        self.lergID.setGeometry(100,50,200,30)
        self.lergPW.setGeometry(100,100,200,30)
        self.lergNa.setGeometry(100,150,200,30)

        self.submit.setGeometry(50,200,250,50)

    def regdit(self):
        connect2 = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
        cur2 = connect2.cursor()
        sql2 = "insert into member values (:id, :pw, :name, 1)"
        cur2.execute(sql2,[self.lergID.text(),self.lergPW.text(),self.lergNa.text()])
        connect2.commit()
        connect2.close()
        QMessageBox.question(self,"가입 끝~~","가입 완료", QMessageBox.Yes, QMessageBox.Yes)
        self.close()

class MyRegisterWindow2(QMainWindow):
    def __init__(self,parent):
        super().__init__(parent)
        self.setCentralWidget(MyWidget(self))
        

class MyWidget(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.setWindowTitle("헬조선 가입")
        self.setGeometry(100,100,350,300)
        self.rglbID = QLabel("ID",self)
        self.rglbPW = QLabel("PW",self)
        self.rglbNa = QLabel("Name",self)

        self.rgleID = QLineEdit(self)
        self.rglePW = QLineEdit(self)
        self.rgleNa = QLineEdit(self)

        self.submit = QPushButton("가입하기",self)
        self.submit.clicked.connect(self.regdit)

        self.vboxlb = QVBoxLayout()
        self.vboxlb.addWidget(self.rglbID)
        self.vboxlb.addWidget(self.rglbPW)
        self.vboxlb.addWidget(self.rglbNa)

        self.vboxle = QVBoxLayout()
        self.vboxle.addWidget(self.rgleID)
        self.vboxle.addWidget(self.rglePW)
        self.vboxle.addWidget(self.rgleNa)

        self.hboxtxt = QHBoxLayout()
        self.hboxtxt.addLayout(self.vboxlb)
        self.hboxtxt.addLayout(self.vboxle)

        vbox = QVBoxLayout()
        vbox.addLayout(self.hboxtxt)
        vbox.addWidget(self.submit)
        self.setLayout(vbox)

    def regdit(self):
        connect2 = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
        connect2.cursor().execute("insert into member values (:id, :pw, :name, 1)",[self.rgleID.text(),self.rglePW.text(),self.rgleNa.text()])
        connect2.commit()
        connect2.close()
        QMessageBox.question(self,"가입 끝~~","가입 완료", QMessageBox.Yes, QMessageBox.Yes)
        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())