import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    user = {"kojunwoan":"naver","ridass":"google"}
    def __init__(self):
        super().__init__()
        self.initUI()
    def print(self):
        if self.leID.text() in self.user:
            if self.user[self.leID.text()] == self.lePW.text():
                print("로그인")
            else:
                print("비번 틀림")
        else:
            print("아이디 없음")
        self.leID.setText("")
        self.lePW.setText("")
    def close(self):
        if QMessageBox.question(self, "메세지", "정말 나갈려구?", QMessageBox.Yes| QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            QCoreApplication.instance().quit()
    def initUI(self):
        #라벨 2개
        labelID = QLabel("ID",self)
        labelPW = QLabel("PW",self)
        #폰트 크게
        font1 = labelID.font()
        font1.setPointSize(30)
        labelID.setFont(font1)

        font2 = labelPW.font()
        font2.setPointSize(30)
        labelPW.setFont(font2)

        labelID.move(300,150)
        labelPW.move(300,250)

        labelID.resize(120,50)
        labelPW.resize(120,50)

        #QlineEdit
        self.leID = QLineEdit(self)
        self.lePW = QLineEdit(self)

        self.leID.move(500,150)
        self.lePW.move(500,250)
        self.leID.resize(120,50)
        self.lePW.resize(120,50)

        #푸쉬버튼 객체 생성
        btn1 = QPushButton("출력",self)
        btn1.setText("LOGIN")
        btn1.resize(120,50)
        btn1.move(300,500)
        btn1.clicked.connect(self.print)

        btn2 = QPushButton("Exit!",self)
        btn2.resize(120,50)
        btn2.move(700,500)
        # btn2.clicked.connect(QCoreApplication.instance().quit)
        btn2.clicked.connect(self.close)

        self.setWindowTitle("불금불금")
        self.move(0,0)
        self.setWindowIcon(QIcon('./img/exit.jpg'))
        self.resize(1280,720)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())