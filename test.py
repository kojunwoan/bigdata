import sys
from PyQt5 import *
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1280,720)
        self.show()


if __name__ =="__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())