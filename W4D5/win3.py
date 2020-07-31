import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def keyPressEvent(self,e):
        if e.key() == 87:
            self.moveup()
        elif e.key() == 65:
            self.movelf()
        elif e.key() == 68:
            self.movert()
        elif e.key() == 83:
            self.movedo()
        elif e.key() == 49:
            self.movelf()
            self.movedo()
        elif e.key() == 50:
            self.movedo()
        elif e.key() == 51:
            self.movert()
            self.movedo()
        elif e.key() == 52:
            self.movelf()
        elif e.key() == 54:
            self.movert()
        elif e.key() == 55:
            self.movelf()
            self.moveup()
        elif e.key() == 56:
            self.moveup()
        elif e.key() == 57:
            self.movert()
            self.moveup()

    def moveup(self):
        self.character.move(self.character.x(),self.character.y()-10)
    def movelf(self):
        self.character.setText("_(:3」∠)_")
        self.character.move(self.character.x()-10,self.character.y())
    def movert(self):
        self.character.setText("_(┐「ε:)_")
        self.character.move(self.character.x()+10,self.character.y())
    def movedo(self):
        self.character.move(self.character.x(),self.character.y()+10)

    def initUI(self):
        p_img = QPixmap("./img/turtle.gif")
        r_img = QPixmap("./img/room.jpg")
        room = QLabel("room",self)
        room.setPixmap(r_img)
        self.resize(1280,720)
        
        upbtn = QPushButton("↑",self)
        lfbtn = QPushButton("←",self)
        rtbtn = QPushButton("→",self)
        dobtn = QPushButton("↓",self)

        upbtn.resize(50,50)
        lfbtn.resize(50,50)
        rtbtn.resize(50,50)
        dobtn.resize(50,50)

        upbtn.move(630,500)
        lfbtn.move(580,550)
        rtbtn.move(680,550)
        dobtn.move(630,600)

        font = upbtn.font()
        font.setPointSize(20)

        upbtn.setFont(font)
        lfbtn.setFont(font)
        rtbtn.setFont(font)
        dobtn.setFont(font)

        self.character = QLabel("_(:3」∠)_",self)
        self.character.move(600,100)
        self.character.resize(350,200)

        chas = self.character.font()
        chas.setPointSize(50)
        chas.setBold(True)
        self.character.setFont(chas)

        
        upbtn.clicked.connect(self.moveup)
        lfbtn.clicked.connect(self.movelf)
        rtbtn.clicked.connect(self.movert)
        dobtn.clicked.connect(self.movedo)






        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())