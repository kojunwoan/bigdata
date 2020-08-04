import cx_Oracle
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from dbConnect import DbConnect

'''
QWidjet
위젯은 한 화면에 표시할 수 있는 것을 목적으로 한다.
윈도우나 버튼 모든 위젯 화면에 무언가를 표시하거나 키보드/마우스에서 사용자의 입력을 받아들이는 것.
버튼, 슬라이드, 뷰, 대화상자 등등 사용자의 상호 작용을 나타내는 사각형 영역


QMainWindow
메인 창에서는 최상위 위젯이고 메뉴바, 도구모음, 상태표시줄 등을 포함하는 미리 정의된 레이아웃을 사용함
창은 부모/자식의 상단이며 일반적으로 제목 표시줄과 테두리를 표시

QDialog
특수한 종류의 창으로 보통 일시적
알림, 입력, 선택
'''


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
        self.labelID.setGeometry(470,150,120,50)
        self.labelPW.setGeometry(470,230,120,50)

        #폰트 크게
        font1 = self.labelID.font()
        font1.setPointSize(30)
        font1.setBold(True)
        self.labelID.setFont(font1)
        self.labelPW.setFont(font1)

        #QlineEdit
        self.leID = QLineEdit(self)
        self.lePW = QLineEdit(self)
        self.leID.setGeometry(550,150,120,50)
        self.lePW.setGeometry(550,230,120,50)

        #푸쉬버튼 객체 생성
        self.btnlogin = QPushButton("헬조선 로그인",self)
        self.btnlogin.setGeometry(550,330,120,50)
        self.btnlogin.clicked.connect(self.dbcheck)

        self.btnreg = QPushButton("헬조선 가입1",self)
        self.btnreg.setGeometry(550,400,120,50)
        self.btnreg.clicked.connect(self.register)
        
        self.btnreg2 = QPushButton("헬조선 가입2",self)
        self.btnreg2.setGeometry(550,450,120,50)
        self.btnreg2.clicked.connect(self.register2)

        self.btnreg3 = QPushButton("헬조선 가입3",self)
        self.btnreg3.setGeometry(550,500,120,50)
        self.btnreg3.clicked.connect(self.register3)

        btnclose = QPushButton("X",self)
        btnclose.setGeometry(660,10,30,30)
        # btnclose.clicked.connect(QCoreApplication.instance().quit)
        btnclose.clicked.connect(self.close)

        self.setWindowTitle("Welcome to Hell Chosun, stranger")
        self.setWindowIcon(QIcon('./img/exit.jpg'))
        self.setGeometry(0,0,720,950)
        self.show()


    def dbcheck(self):
        #1. connection 객체 생성
        db = DbConnect("scott","tiger","192.168.0.68","orcl")
        #2. cursor 객체 생성
        #3. 사용할 sql문 객체
        #4. 실행
        print(db.execute("select id from member where id = '{}' and pw = '{}'".format(self.leID.text(),self.lePW.text())))
        #5. 로직처리
        #6. 자원 반납
    def login(self):
        pass
    def register(self):
        self.nw1 = MyRegisterWindow1(self)
        self.nw1.show()
    def register2(self):
        self.nw2 = MyRegisterWindow2(self)
        self.nw2.show()
    def register3(self):
        self.nw3 = MyRegisterWindow3(self)
        self.nw3.show()

    def close(self):
        if QMessageBox.question(self, "메세지", "정말 나갈려구?", QMessageBox.Yes| QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            QCoreApplication.instance().quit()

class MyRegisterWindow1(QMainWindow):
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
        connect2.cursor().execute("insert into member values (:id, :pw, :name, 1)",[self.lergID.text(),self.lergPW.text(),self.lergNa.text()])
        connect2.commit()
        connect2.close()
        QMessageBox.question(self,"가입 끝~~","가입 완료", QMessageBox.Yes, QMessageBox.Yes)
        self.close()

class MyRegisterWindow2(QMainWindow):
    def __init__(self,parent):
        super().__init__(parent)
        self.setWindowTitle("헬조선 가입2")
        self.setCentralWidget(MyWidget2(self))
        

class MyWidget2(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.setGeometry(100,100,350,300)
        self.rglbID = QLabel("ID",self)
        self.rglbPW = QLabel("PW",self)
        self.rglbNa = QLabel("Name",self)

        self.rgleID = QLineEdit(self)
        self.rglePW = QLineEdit(self)
        self.rgleNa = QLineEdit(self)

        self.submit = QPushButton("가입하기",self)
        self.submit.clicked.connect(self.regdit)
        '''
        LayOut, BoxLayout, 수평상자 수직상자
        '''
        vboxlb = QVBoxLayout()
        vboxlb.addWidget(self.rglbID)
        vboxlb.addWidget(self.rglbPW)
        vboxlb.addWidget(self.rglbNa)

        vboxle = QVBoxLayout()
        vboxle.addWidget(self.rgleID)
        vboxle.addWidget(self.rglePW)
        vboxle.addWidget(self.rgleNa)

        hboxtxt = QHBoxLayout()
        hboxtxt.addLayout(vboxlb)
        hboxtxt.addLayout(vboxle)

        vbox = QVBoxLayout()
        vbox.addLayout(hboxtxt)
        vbox.addWidget(self.submit)
        self.setLayout(vbox)

    def regdit(self):
        connect2 = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
        connect2.cursor().execute("insert into member values (:id, :pw, :name, 1)",[self.rgleID.text(),self.rglePW.text(),self.rgleNa.text()])
        connect2.commit()
        connect2.close()
        QMessageBox.question(self,"가입 끝~~","가입 완료", QMessageBox.Yes, QMessageBox.Yes)
        self.parent.close()




class MyRegisterWindow3(QMainWindow):
    def __init__(self,parent):
        super().__init__(parent)
        self.setWindowTitle("헬조선 가입3")
        self.setCentralWidget(MyWidget3(self))
        

class MyWidget3(QWidget):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.setGeometry(100,100,350,300)
        self.rglbID = QLabel("ID",self)
        self.rglbPW = QLabel("PW",self)
        self.rglbNa = QLabel("Name",self)

        self.rgleID = QLineEdit(self)
        self.rglePW = QLineEdit(self)
        self.rgleNa = QLineEdit(self)

        self.submit = QPushButton("가입하기",self)
        self.submit.clicked.connect(self.regdit)
        '''
        그리드 레이아웃
        '''
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.rglbID,0,0)
        grid.addWidget(self.rgleID,0,1)
        grid.addWidget(self.rglbPW,1,0)
        grid.addWidget(self.rglePW,1,1)
        grid.addWidget(self.rglbNa,2,0)
        grid.addWidget(self.rgleNa,2,1)
        grid.addWidget(self.submit,3,0,1,2)

    def regdit(self):
        connect2 = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
        connect2.cursor().execute("insert into member values (:id, :pw, :name, 1)",[self.rgleID.text(),self.rglePW.text(),self.rgleNa.text()])
        connect2.commit()
        connect2.close()
        QMessageBox.question(self,"가입 끝~~","가입 완료", QMessageBox.Yes, QMessageBox.Yes)
        self.parent.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())