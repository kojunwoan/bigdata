import sys
from PyQt5 import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        keyL = ['0','00','=','/','1','2','3','*','4','5','6','-','7','8','9','+']
        self.le = QLineEdit(self)
        self.btn = [QPushButton(key,self) for key in keyL]
        hbox = [QHBoxLayout() for i in range(5)]

        for i in range(16):
            hbox[i//4].addWidget(self.btn[i])
        hbox[4].addWidget(self.le)

        vbox = QVBoxLayout()
        for i in range(4,-1,-1):
            vbox.addLayout(hbox[i])
        self.setLayout(vbox)

        # 눌렀을때 이벤트 만들기
        # self.btn[0].clicked.connect(self.f0)
        '''
        self.btn[0].clicked.connect(lambda : self.func(self.btn[0].text()))     #0
        self.btn[1].clicked.connect(lambda : self.func(self.btn[1].text()))     #00
        self.btn[4].clicked.connect(lambda : self.func(self.btn[4].text()))     #1
        self.btn[5].clicked.connect(lambda : self.func(self.btn[5].text()))     #2
        self.btn[6].clicked.connect(lambda : self.func(self.btn[6].text()))     #3
        self.btn[8].clicked.connect(lambda : self.func(self.btn[8].text()))     #4
        self.btn[9].clicked.connect(lambda : self.func(self.btn[9].text()))     #5
        self.btn[10].clicked.connect(lambda : self.func(self.btn[10].text()))   #6
        self.btn[12].clicked.connect(lambda : self.func(self.btn[12].text()))   #7
        self.btn[13].clicked.connect(lambda : self.func(self.btn[13].text()))   #8
        self.btn[14].clicked.connect(lambda : self.func(self.btn[14].text()))   #9
        '''
        for i in range(len(self.btn)):
            self.btn[i].clicked.connect(lambda : self.func(self.btn[i].text()))



        self.setWindowTitle("계산기")
        self.show()
    def func(self,txt):
        # self.le.setText(self.le.text()+txt)
        print(txt)


    def keyPressEvent(self,e):
        print("키보드가 눌릴때")
    def keyReleaseEvent(self,e):
        print("키보드를 뗄때 동작")
    def mouseMoveEvent(self,e):
        print("마우스를 움직일때 호출")
    def mouseDoubleClickEvent(self,e):
        print("마우스를 더블클릭 했을 때 호출")
    def resizeEvent(self,e):
        print("위젯의 크기를 변경했을때 호출")

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())  
