import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def print(self):
        print("왜 눌럿!")

    def initUI(self):
        #창의 타이틀 지정
        self.setWindowTitle("불금이다 놀러가자")
        self.resize(1280,720)
        self.move(300,400)

        btn1 = QPushButton("가자!",self)
        btn1.setText("print")
        btn1.resize(150,100)
        btn1.move(300,200)
        #이벤트 핸들러
        btn1.clicked.connect(self.print)

        btn2 = QPushButton("안녕~",self)
        btn2.setText("exit")
        btn2.move(500,200)
        btn2.resize(150,100)
        btn2.clicked.connect(QCoreApplication.instance().exit)

        #화면의 창을 보여지게 설정
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
