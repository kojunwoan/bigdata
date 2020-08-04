import sys
from PyQt5 import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        keyL = ['0','00','=','/','1','2','3','*','4','5','6','-','7','8','9','+']
        self.lb = QLabel("",self)
        self.le = QLineEdit(self)
        self.btn = [QPushButton(key,self) for key in keyL]
        hbox = [QHBoxLayout() for i in range(4)]

        for i,btn in enumerate(self.btn):
            hbox[i//4].addWidget(btn)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addWidget(self.le)
        for i in range(3,-1,-1):
            vbox.addLayout(hbox[i])
        self.setLayout(vbox)

        # 눌렀을때 이벤트 만들기
        # self.btn[0].clicked.connect(self.f0)
        self.btn[0].clicked.connect(lambda : self.func(self.btn[0].text()))     #0
        self.btn[1].clicked.connect(lambda : self.func(self.btn[1].text()))     #00
        self.btn[2].clicked.connect(lambda : self.func(self.btn[2].text()))     #=
        self.btn[3].clicked.connect(lambda : self.func(self.btn[3].text()))     #/
        self.btn[4].clicked.connect(lambda : self.func(self.btn[4].text()))     #1
        self.btn[5].clicked.connect(lambda : self.func(self.btn[5].text()))     #2
        self.btn[6].clicked.connect(lambda : self.func(self.btn[6].text()))     #3
        self.btn[7].clicked.connect(lambda : self.func(self.btn[7].text()))     #*
        self.btn[8].clicked.connect(lambda : self.func(self.btn[8].text()))     #4
        self.btn[9].clicked.connect(lambda : self.func(self.btn[9].text()))     #5
        self.btn[10].clicked.connect(lambda : self.func(self.btn[10].text()))   #6
        self.btn[11].clicked.connect(lambda : self.func(self.btn[11].text()))   #-
        self.btn[12].clicked.connect(lambda : self.func(self.btn[12].text()))   #7
        self.btn[13].clicked.connect(lambda : self.func(self.btn[13].text()))   #8
        self.btn[14].clicked.connect(lambda : self.func(self.btn[14].text()))   #9
        self.btn[15].clicked.connect(lambda : self.func(self.btn[15].text()))   #+
        # [btn.clicked.connect(lambda : self.func(btn.text())) for btn in self.btn]

        self.setWindowTitle("계산기")
        self.show()
    def func(self,txt):
        if 48<=ord(txt)<=57:
            self.le.setText(self.le.text()+txt)
        elif txt == "=":
            self.lb.setText(str(eval(self.lb.text()+self.le.text())))
            self.le.setText("")
        else:
            self.lb.setText(self.le.text()+txt)
            self.le.setText("")

    def keyPressEvent(self,e):
    #     print("키보드가 눌릴때")
        if e.key() == 16777216:
            self.le.setText("")
            self.lb.setText("")
    # def keyReleaseEvent(self,e):
    #     print("키보드를 뗄때 동작")
    # def mouseMoveEvent(self,e):
    #     print("마우스를 움직일때 호출")
    # def mouseDoubleClickEvent(self,e):
    #     print("마우스를 더블클릭 했을 때 호출")
    # def resizeEvent(self,e):
    #     print("위젯의 크기를 변경했을때 호출")

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())  
