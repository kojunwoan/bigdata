import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,1280,720)

        gb = [QGroupBox(i) for i in ["타입","Pen Setting","뷰 설정"]]            

        #그룹1 

        box1 = QVBoxLayout()
        gb[0].setLayout(box1)
        for i in ["직선","곡선","사각형","타원"]:
            box1.addWidget(QRadioButton(i,self))

        #그룹2
        gridL = [QLabel("선 굵기"),QComboBox(),QLabel("선색"),QPushButton()]
        grid = QGridLayout()
        gb[1].setLayout(grid)
        for i in range(1,21):
            gridL[1].addItem(str(i))
        self.pencolor = QColor(0,0,0)
        gridL[3].setStyleSheet("Background-color : rgb(0,0,0)")
        for i in range(2):
            for j in range(2):
                grid.addWidget(gridL[i*2+j],i,j)

        #그룹3
        hboxL = [QLabel("붓색상"),QPushButton()]
        hbox = QHBoxLayout()
        gb[2].setLayout(hbox)
        self.brushcolor = QColor(255,255,255)
        hboxL[1].setStyleSheet("Background-color : rgb(255,255,255)")
        for val in hboxL:
            hbox.addWidget(val)
        inbox = [QVBoxLayout() for i in range(2)]

        #좌측묶기
        for i in gb:
            inbox[0].addWidget(i)
        #우측   
        self.view = CGView(self)
        inbox[1].addWidget(self.view)

        frmbox = QHBoxLayout()
        frmbox.addLayout(inbox[0])
        frmbox.addLayout(inbox[1])

        self.setLayout(frmbox)

        self.show()

#QGraphics 는 시각적 객체의 복잡한 장면을 쉽게 처리 할수 있는 프레임 워크로 구성하는데 사용 할 수 있다
#QGraphicsView, QGraphicsScene, QGraphicsItem

class CGView(QGraphicsView):
    def __init__(self,parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.items = []
        self.start = QPointF()
        self.end = QPointF()


if __name__=="__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())