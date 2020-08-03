import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "취업 지원"
        self.setGeometry(200,200,300,300)
        self.btn = QPushButton("비법 자소서 보기",self)
        self.btn.move(100,100)
        self.btn.setToolTip("<h3>날 눌러봐!!</h3>")
        self.btn.clicked.connect(self.newWindow)
        self.show()

    def newWindow(self):
        for i in range(5):
            time.sleep(0.2)
            self.nw = MyWindow2(self)
            self.nw.move(100+i*10,100+i*10)
            self.nw.show()

class MyWindow2(QMainWindow):
    def __init__(self, parent):
        super(MyWindow2, self).__init__(parent)
        self.setGeometry(100,100,300,300)
        p_img = QPixmap("./img/merong.jpeg")
        self.lb = QLabel("메롱",self)
        self.lb.setPixmap(p_img)
        self.lb.setGeometry(0,0,200,200)
        self.show()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())