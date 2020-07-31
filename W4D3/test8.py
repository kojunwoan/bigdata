#상속
class Person:
    '''
    인간 클래스
    '''
    def __init__(self):
        print("초기화 함수")
        print(id(self))
        self.name = "홍길동"
        self.age = 20
        self.job = "도적"

    def eating(self, what):
        print(self.name+ "이", what, "을/를 맛있게 먹어요.")

    def sleeping(self):
        print("쿨쿨")

# Person 클래스를 상속받은 Superman 클래스

class Superman(Person):

    def __init__(self,name,age,job,hobby):
        self.name = name
        self.age = age
        self.job = job
        self.hobby = hobby

    def fly(self):
        print("비행")
        print("비행청소년??")

    def laser(self):
        print("레이저 발사!")

sm = Superman('슈퍼맨',20,'기자','연애')
sm.fly()
sm.laser()
sm.eating('바나나')
sm.sleeping()