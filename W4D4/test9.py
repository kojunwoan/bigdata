# 필요한 함수의 패키지 설치하기
# 1) pypi.org->pyqt5 검색->첫번째 것 클릭..등등 하는 방법
# 2) 터미널 창에 설치하기
#   dir/w
#   ls
#   pip install pyqt5                                       # pip install 패키지명
#=> 경고: 현재 내 프로그램 버전과 패키지 버전이 맞지않음
#   python.exe -m pip install --upgrade pip                 # 가장 최신버전으로 갱신(안해도 괜찮은 단계)

import sys                                               # 시스템접근을 위한 패키지(sys) 가져오기
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton        # 해당패키지(PyQt5)에서 widget만 모은 것들에서
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        btn = QPushButton("나가기",self)
        btn.move(100,100)
        btn.resize(200,150)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("내가 만든 윈도우창")           # 윈도우창에 이름 부여
        self.move(10,10)                                    # 창이 시작(열리는) 위치 지정
        self.setWindowIcon(QIcon("./img/instagram.png"))
        self.resize(1200,600)                               # 창 사이즈 조절
        self.show()                                         # 해당창이 보여지게

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())