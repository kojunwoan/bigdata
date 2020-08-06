import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import time
import threading
class MyApp(QWidget):
    img_link = ["./img/room.jpg","./img/bed.webp","./img/grass.jpeg"]
    i = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    def keyPressEvent(self,e):
        if e.key() in [87,Qt.Key_Up,56]:
            self.moveup()
        elif e.key() in [65,Qt.Key_Left,52]:
            self.movelf()
        elif e.key() in [68,Qt.Key_Right,54]:
            self.movert()
        elif e.key() in [83,Qt.Key_Down,50]:
            self.movedo()
        elif e.key() == 49:
            self.movelf()
            self.movedo()
        elif e.key() == 51:
            self.movert()
            self.movedo()
        elif e.key() == 55:
            self.movelf()
            self.moveup()
        elif e.key() == 57:
            self.movert()
            self.moveup()
        elif e.key() == Qt.Key_Space:
            # self.changemap()
            threading.Thread(target=self.moveTurtle).start()
            # threading.Thread(target=self.moveSpaceX).start()
            # threading.Thread(target=self.moveSpaceY).start()
    def moveTurtle(self):
        cx = self.character.x()
        cy = self.character.y()
        y = 0
        for x in range(2,40,2):
            y = -x**2 +2*x
            self.character.move(cx+x,cy+y)
            time.sleep(0.03)


    def moveSpaceX(self):
        for i in range(11):
            if self.character.text() == "_(┐「ε:)_":
                self.movert(20)
            else:
                self.movelf(20)
            time.sleep(0.03)
    def moveSpaceY(self):
        print("스페이스 눌림")
        h = 30
        for i in range(11):
            self.moveup(h)
            h -= 6
            time.sleep(0.03)

    def changemap(self):
        self.i += 1
        if self.i == len(self.img_link):
            self.i = 0
        self.img.setPixmap(QPixmap(self.img_link[self.i]))
    def moveup(self,l=10):
        self.character.move(self.character.x(),self.character.y()-l)
    def movelf(self,l=10):
        self.character.setText("_(:3」∠)_")
        self.character.move(self.character.x()-l,self.character.y())
    def movert(self,l=10):
        self.character.setText("_(┐「ε:)_")
        self.character.move(self.character.x()+l,self.character.y())
    def movedo(self,l=10):
        self.character.move(self.character.x(),self.character.y()+l)

    def initUI(self):
        p_img = QPixmap("./img/turtle.gif")
        r_img = QPixmap(self.img_link[self.i])
        self.img = QLabel("room",self)
        self.img.setPixmap(r_img)
        self.resize(1280,720)
        
        self.character = QLabel("_(:3」∠)_",self)
        self.character.move(500,300)
        self.character.resize(320,70)

        chas = self.character.font()
        chas.setPointSize(50)
        chas.setBold(True)
        self.character.setFont(chas)

        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())