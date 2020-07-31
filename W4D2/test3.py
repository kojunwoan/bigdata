class Human:
    def __init__(self):
        print('초기화 함수')
        self.name = "고길동"
        self.age = 30
        self.job = '고위공직자'
        self.eye = 2
        self.mouse = 1
        self.ears = 2

    def eating(self):
        print("먹어요")

    def walking(self):
        print("걸어요")

    def sleeping(self):
        print("자요")

    def thinking(self):
        print("생각해요")

    def status(self):
        print("이름 : ",self.name)
        print("나이 : ",self.age)
        print("직업 : ",self.job)
        print("눈 : ",self.eye )
        print("입 : ",self.mouse )
        print("귀 : ",self.ears)
        
print(Human, id(Human), type(Human))

ko = Human() #인스턴스 변수 = 클래스명() <- 클래스의 초기화 함수 호출

print(ko.name)
ko.thinking()
ko.status()

pen = Human()
pen.name = "팽수"
pen.age = 10
pen.job = "엔터테이너"
pen.status()