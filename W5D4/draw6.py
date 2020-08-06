import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import randint
from time import sleep
from threading import Thread

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 창 타이틀
        self.setWindowTitle("점찍기")
        # 크기와 위치
        self.setGeometry(100,100,800,800)
        # 화면에 보이게 설정
        self.show()

    def paintEvent(self, e):
        # # print("페인트 이벤트 발생@@_@@_@@_@")
        # for i in range(1000):
        self.qp = QPainter()
        self.qp.begin(self)
        Thread(target=self.paint).start()
        self.qp.end()
    
    def paint(self):
        # Qpaint 인스턴스 생성
        # 페인팅 시작
        for i in range(100):
            Thread(target=self.paint2).start()
            sleep(0.1)
        # 펜 설정(펜객체(색상,크기))
    def paint2(self):
        self.qp.setPen(QPen(QColor(randint(0,255),randint(0,255),randint(0,255)), randint(1,10)))
        # 펜위치(화면너비 절반, 화면높이 절반)
        self.qp.drawLine(randint(0,800),randint(0,800),randint(0,800),randint(0,800))
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())