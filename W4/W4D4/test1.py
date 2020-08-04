class Car:
    def __init__(self, handle=1, wheel=4, eye=2, nose=1, mouse=1):
        self.handle = handle
        self.wheel = wheel
        self.eye = eye
        self.nose = nose
        self.mouse = mouse
        print("초기화 함수 호출")

    def run(self):
        print(self.wheel, "붕붕카 달리는중")
    def stop(self):
        print("정지..")
    def smell(self, what):
        print(what, "냄새를 맡는중")
    def talk(self):
        print("혼자 중얼중얼 대화중입니다.")
    def __add__(self,otherCar): #연산자+(add)를 오버로딩
        print("충돌났네요 ㅠㅜ")
    def __sub__(self,otherCar):
        print("왜 빼는거지...")

class InheritedCar(Car):
    def lightOn(self):
        print("라이트를 켜요")

    def run(self):
        print("오픈카로 달려요")


c1 = Car()
ic1 = InheritedCar()
c1.smell("꽃")
c1.run()
ic1.smell("장미") #냄새맡는 오픈카 ㅋㅋ
ic1.lightOn()
ic1.run()

c1 + ic1#18line