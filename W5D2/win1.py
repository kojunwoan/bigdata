import sys
from PyQt5.QtWidgets import *

def quit():
    print("quit() 호출됨")
    sys.exit(0)         #0이 정상종료 나머지??? 비정상종료


# QApplication 클래스의 인스턴스를 생성
app = QApplication(sys.argv)
print(app, sys.argv)
btn = QPushButton("QUIT")
btn.show()
btn.clicked.connect(quit)

app.exec_()