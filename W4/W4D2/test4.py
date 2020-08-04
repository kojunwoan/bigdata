class Human:
    def __init__(self,a,b,c):
        print('초기화 함수')
        self.name = a
        self.age = b
        self.job = c
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


p = Human("팽수",10,"엔터테이너")
d = Human("둘리",100000000,"고아")

class Car:
    def __init__(self,brand,model,color,year):
        print("초기화 함수 호출")
        self.brand = brand        #인스턴스 변수
        self.model = model
        self.color = color
        self.year = year
        self.tire=4
        self.handle=1
    def forward(self):      #인스턴스 함수(메서드)
        print("전진 합니다.")
    def back(self):
        print("후진 합니다.")
    def lighting(self):
        print("깜박이 킵니다")
    def acceling(self):
        print("가속 합니다.")
    def diceling(self):
        print("감속 합니다.")
    def stop(self):
        print("정지합니다.")
    def status(self):
        print("제조사 :",self.brand)
        print("차명 :",self.model)
        print("색상 :",self.color)
        print("연식 :",self.year)
        print("바퀴 :",self.tire)
        print("핸들 :",self.handle)

c=Car("Volvo","volvo C90","black",30)
c.status()

ns = Car("닛산","맥시마","silver",2019)
ns.status()

#메서드의 첫번째 파라미터명은 관례적으로 self 이름 사용
#호출시 호출한 객체 자신이 전달되기 때문 self 이름 사용

c.forward()
ns.forward()
Car.forward(c)