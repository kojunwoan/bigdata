import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import randint
from threading import Thread
from time import sleep

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() #초기상태로 만든다
        self.setGeometry(100,100,1280,720)
        self.show()

    def initUI(self):
        self.lbL = [QLabel("q",self) for i in range(6)]
        self.thread = []
        grid = QGridLayout()
        for lb in self.lbL:
            lb.setPixmap(QPixmap("./img/lotto/q.jpg"))
            grid.addWidget(lb,0,self.lbL.index(lb))

        self.btn = QPushButton("대박번호")
        self.btn.clicked.connect(self.btnevent)
        grid.addWidget(self.btn,1,2,2,2)
        self.setLayout(grid)

    def btnevent(self):
        self.btn.setText("추첨하기!")
        self.l = set()
        while len(self.l)<6:
            self.l.add(randint(1,45))
        self.thread = [Thread(target=self.spinball, args=(self.lbL[i],num)).start() for i, num in enumerate(l)]

    def spinball(self,lb,n):
        lb.setPixmap(QPixmap("./img/lotto/ball"+str(n)+".png"))
        sleep(0.05)

    

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())