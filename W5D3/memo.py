import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.txtEdit = QTextEdit()
        self.setWindowTitle("제목 없음 - Window 메모장")
        self.setWindowIcon(QIcon("./img/notepad.png"))
        self.setGeometry(100,100,1280,720)
        self.setCentralWidget(self.txtEdit)

        newFile = QAction(QIcon("./img/notepad.png"),"새 파일",self)
        newFile.setShortcut("Ctrl+N")
        newFile.setStatusTip("새 파일 만들기")
        newFile.triggered.connect(self.newFile)

        openFile = QAction(QIcon("./img/open-file-icon.png"),"열기",self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("파일 열기")
        openFile.triggered.connect(self.showDialog)

        saveFile = QAction(QIcon("./img/notepad.png"),"저장",self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("파일 저장")
        saveFile.triggered.connect(self.saveDialog)

        closeFile = QAction(QIcon("./img/notepad.png"),"종료",self)
        closeFile.setShortcut("Ctrl+C")
        closeFile.setStatusTip("파일 종료")
        closeFile.triggered.connect(lambda : self.close())

        #서식메뉴

        fontMenu = QAction(QIcon("./img/notepad.png"),"글꼴",self)
        fontMenu.setShortcut("Ctrl+F")
        fontMenu.setStatusTip("글꼴")
        fontMenu.triggered.connect(self.changeFont)



        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu("&파일")
        fileMenu.addAction(newFile)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(closeFile)

        formMenu = menubar.addMenu("&서식")
        formMenu.addAction(fontMenu)

        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,"open file","./")
        if fname[0]:
            with open(fname[0],'r'):
                self.txtEdit.setText(open(fname[0],'r').read())
                self.setWindowTitle(fname[0].split("/")[-1].split(".")[0]+"- Window 메모장")

    def saveDialog(self):
        file = QFileDialog.getSaveFileName(self,"저장","./")
        if file[0].find(".") == -1:
            file = list(file)
            file[0] += ".txt"
            file = tuple(file)
        with open(file[0],'w') as f:
            f.write(self.txtEdit.toPlainText())
            self.setWindowTitle(file[0].split("/")[-1].split(".")[0]+"- Window 메모장")

    
    def newFile(self):
        if self.txtEdit.toPlainText():
            if QMessageBox.question(self,"메모장","변경 내용을 저장하시겠습니까?",QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel,QMessageBox.Cancel) == QMessageBox.Yes:
                self.saveDialog()
        self.txtEdit.setText("")

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.txtEdit.setFont(font)
if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())