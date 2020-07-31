import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def print3dan(self):
        msg=""
        for i in range(1,10):
            msg+="3 * {} = {}\n".format(i,3*i)
        

    def initUI(self):
        self.setWindowTitle("구구단")
        self.resize(800,600)
        
        btn = QPushButton("출력",self)
        btn.resize(100,100)
        btn.move(350,250)
        btn.clicked.connect(self.print3dan)

        label = QLabel("",self)
        

        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())