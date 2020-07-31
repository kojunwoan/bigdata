import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel("집에가자~~~~",self)
        font1 = label1.font()
        font1.setPointSize(50)
        label1.setFont(font1)

        label1.move(400,250)

        hwbtn = QPushButton("정신차리고 숙제하기",self)
        hwbtn.resize(150,50)
        hwbtn.move(550,100)

        ghbtn = QPushButton("Go!",self)
        font2 = ghbtn.font()
        font2.setPointSize(30)
        ghbtn.setFont(font2)
        ghbtn.resize(1000,150)
        ghbtn.move(140,400)
        ghbtn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("집가고싶어")
        self.move(0,0)
        self.setWindowIcon(QIcon('./img/exit.jpg'))
        self.resize(1280,720)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())