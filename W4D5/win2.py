import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def printdan(self):
        for i in range(1,10):
            print("{} * {} = {}".format(self.le.text(),i,int(self.le.text())*i))
        
        

    def initUI(self):
        self.setWindowTitle("구구단")
        self.resize(800,600)
        
        btn = QPushButton("출력",self)
        btn.resize(100,100)
        btn.move(350,350)
        btn.clicked.connect(self.printdan)

        self.label = QLabel("",self)
        self.label.move(100,100)

        self.le = QLineEdit(self)

        self.le.move(350,250)
        self.le.resize(100,50)

        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())