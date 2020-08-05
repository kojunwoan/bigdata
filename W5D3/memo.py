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

        openFile = QAction(QIcon("./img/open-file-icon.png"),"열기",self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("파일 열기")

        saveFile = QAction(QIcon("./img/notepad.png"),"저장",self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("파일 저장")

        closeFile = QAction(QIcon("./img/notepad.png"),"종료",self)
        closeFile.setShortcut("Ctrl+X")
        closeFile.setStatusTip("파일 종료")

        #새파일 만들기
        #열기
        #저장
        #종료

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(newFile)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(closeFile)




        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())