import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #좌측 만들기
        gbL = [QGroupBox(i) for i in ["타입","Pen Setting","뷰 설정","File"]]            
        leftlayoutL = [QVBoxLayout(),QGridLayout(),QHBoxLayout(),QVBoxLayout()]
        #그룹1---------------------------------------
        self.radio = [QRadioButton(i,self) for i in ["직선","사각형","곡선","타원","지우개"]]
        [leftlayoutL[0].addWidget(r) for r in self.radio]
        self.radio[0].setChecked(True)
        self.drawType = 0
        [self.radioBtnClicked(r,i) for i,r in enumerate(self.radio)]    #라디오버튼 체크시 drawType 변경
        #그룹2---------------------------------------
        self.gridL = [QLabel("선 굵기"),QComboBox(),QLabel("선색"),QPushButton()]
        [self.gridL[1].addItem(str(i)) for i in range(1,21)]
        self.pencolor = QColor(0,0,0)
        self.gridL[3].setStyleSheet("Background-color : rgb(0,0,0)")
        self.gridL[3].clicked.connect(self.selectColorDlg)
        [leftlayoutL[1].addWidget(self.gridL[i*2+j],i,j) for i in range(2) for j in range(2)]
        #그룹3---------------------------------------
        self.hboxL = [QLabel("붓색상"),QPushButton()]
        self.brushcolor = QColor(255,255,255)
        self.hboxL[1].setStyleSheet("Background-color : rgb(255,255,255)")
        self.hboxL[1].clicked.connect(self.selectColorDlg)
        [leftlayoutL[2].addWidget(val) for val in self.hboxL]
        #그룹4---------------------------------------
        btnL = [QPushButton(n,self) for n in ["새로만들기","저장"]]
        btnL[0].clicked.connect(self.new_img)
        btnL[1].clicked.connect(self.save_img)
        [leftlayoutL[3].addWidget(btn) for btn in btnL]
        #좌측묶기---------------------------------------
        inbox = [QVBoxLayout() for i in range(2)]
        for i,gb in enumerate(gbL):
            inbox[0].addWidget(gb)
            gb.setLayout(leftlayoutL[i])
        #우측---------------------------------------
        self.view = CGView(self)
        inbox[1].addWidget(self.view)
        #전체묶기---------------------------------------
        frmbox = QHBoxLayout()
        frmbox.addLayout(inbox[0])
        frmbox.addLayout(inbox[1])
        self.items = []
        self.setLayout(frmbox)
        self.setGeometry(100,100,1280,720)
        self.show()

    def radioBtnClicked(self,radio,index):
        radio.clicked.connect(lambda : self.radiocl(radio,index))
    def radiocl(self,radio,index):
        if radio.isChecked:
            self.drawType = index
    def selectColorDlg(self):
        color = QColorDialog.getColor()
        if self.sender() == self.gridL[3]:
            self.pencolor = color
            self.gridL[3].setStyleSheet("Background-color:{}".format(color.name()))
        else:
            self.brushcolor = color
            self.hboxL[1].setStyleSheet("Background-color : {}".format(color.name()))
    def new_img(self):
        if self.items:
            msg = QMessageBox.question(self,"그림판","변경 내용을 저장하시겠습니까?",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Yes)
            if msg == QMessageBox.Cancel:
                return
            elif msg == QMessageBox.Yes:
                self.save_img()
            self.items = []
            self.view.scene.clear()

    def save_img(self):
        fname = QFileDialog.getSaveFileName(self,"어디다가 저장하니??","./")
        if fname[0]:
            if fname[0].find('.') == -1:
                fname = list(fname)
                fname[0]+=".png"
            QPixmap(self.view.grab(self.view.sceneRect().toRect())).save(fname[0])

class CGView(QGraphicsView):
    def __init__(self,parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.start = QPointF()
        self.end = QPointF()

    def moveEvent(self,e):  #창크기 변경
        rect = QRectF(self.rect())
        rect.adjust(0,0,-3,-3)
        self.scene.setSceneRect(rect)
    def mousePressEvent(self,e):
        if e.button()==Qt.LeftButton:
            self.start = e.pos()
            self.end = e.pos()
            if len(self.parent().items):     #드레그중 일어난 이벤트로 인해 생성된 선 제거
                self.scene.removeItem(self.parent().items[-1])
                del(self.parent().items[-1])
            if self.parent().drawType == 4:
                rect = QRectF(e.pos().x()-self.parent().gridL[1].currentIndex(),e.pos().y()-self.parent().gridL[1].currentIndex(),self.parent().gridL[1].currentIndex()*2,self.parent().gridL[1].currentIndex()*2)
                self.parent().items.append(self.scene.addRect(rect,QPen(Qt.black,5),QBrush(Qt.white)))
                self.scene.addRect(rect,QPen(Qt.white,0),QBrush(Qt.white))
    
    def mouseMoveEvent(self,e):
        if len(self.parent().items):     #드레그중 일어난 이벤트로 인해 생성된 선 제거
            self.scene.removeItem(self.parent().items[-1])
            del(self.parent().items[-1])
        self.end = e.pos()
        pen = QPen(self.parent().pencolor,self.parent().gridL[1].currentIndex())
        line = QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
        brush = QBrush(self.parent().brushcolor)
        rect = QRectF(min(self.start.x(),self.end.x()),min(self.start.y(),self.end.y()),abs(self.start.x()-self.end.x()),abs(self.start.y()-self.end.y()))
        if self.parent().drawType == 0:
            self.parent().items.append(self.scene.addLine(line, pen))
        elif self.parent().drawType == 1:
            self.parent().items.append(self.scene.addRect(rect,pen,brush))
        elif self.parent().drawType == 2:
            self.scene.addLine(line, pen)
            self.start = e.pos()
        elif self.parent().drawType == 3:
            self.parent().items.append(self.scene.addEllipse(rect,pen,brush))
        elif self.parent().drawType == 4:
            rect = QRectF(e.pos().x()-self.parent().gridL[1].currentIndex(),e.pos().y()-self.parent().gridL[1].currentIndex(),self.parent().gridL[1].currentIndex()*2,self.parent().gridL[1].currentIndex()*2)
            self.parent().items.append(self.scene.addRect(rect,QPen(Qt.black,5),QBrush(Qt.white)))
            self.scene.addRect(rect,QPen(Qt.white,0),QBrush(Qt.white))

    def mouseReleaseEvent(self,e):
        self.end = e.pos()
        pen = QPen(self.parent().pencolor,self.parent().gridL[1].currentIndex())
        line = QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
        brush = QBrush(self.parent().brushcolor)
        rect = QRectF(min(self.start.x(),self.end.x()),min(self.start.y(),self.end.y()),abs(self.start.x()-self.end.x()),abs(self.start.y()-self.end.y()))
        if self.parent().drawType == 0:
            self.scene.addLine(line,pen)
        elif self.parent().drawType == 1:
            self.scene.addRect(rect,pen,brush)
        elif self.parent().drawType == 2:
            self.parent().items.append(self.scene.addLine(line, pen))
        elif self.parent().drawType == 3:
            self.scene.addEllipse(rect,pen,brush)

if __name__=="__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())