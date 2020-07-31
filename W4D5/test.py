import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def printdan(self):
        for i in range(1,10):
            print("{} * {} = {}".format(3,i,3*i))

    def initUI(self):
        self.setWindowTitle("구구단")
        self.resize(800,600)

        btn=QPushButton("출력",self)
        btn.move(350,250)
        btn.resize(100,50)
        

        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())