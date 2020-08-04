import sys
from PyQt5 import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        keyL = ['0','00','=','/','1','2','3','*','4','5','6','-','7','8','9','+']
        self.lb, self.le = QLabel("",self), QLabel("",self)
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

        for btn in self.btn:
            self.click(btn,btn.text())  # 버튼 눌렀을때 이벤트 만들기 

        self.setWindowTitle("계산기")
        self.show()

    def click(self,btn,txt):
        btn.clicked.connect(lambda : self.func(txt))
    def func(self,txt):
        if txt == "00":
            self.le.setText(self.le.text()+txt)
        elif 48<=ord(txt)<=57:
            self.le.setText(self.le.text()+txt)
        elif txt == "=":
            self.lb.setText(str(eval(self.lb.text()+self.le.text())))
            self.le.setText("")
        else:
            self.lb.setText(self.le.text()+txt)
            self.le.setText("")
    def keyPressEvent(self,e):
        if e.key() == 16777216:     #esc 눌렀을때 초기화
            self.le.setText("")
            self.lb.setText("")
    #     print("키보드가 눌릴때")
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