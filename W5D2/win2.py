import sys
from PyQt5.QtWidgets import *

#윈도우를 생성하는 클래스 : QMainWindow, QWidget, QDialog
#메인윈도우를 생성하기 위한 클래스: QMainWindow, QDialog
#QMainWindow : QHBoxLayout, QVBoxLayout 사용 불가

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())       #app.exec_() : 이벤트루프 -> 종료시 0 // sys.exit(0)되면 정상종료