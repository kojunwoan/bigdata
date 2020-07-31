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

p1 = Person()
print(p1.name, p1.age, p1.job)

p1.eating("coffee")

p2 = Person()
print(p2.name)
print("id(p1)" , id(p1), "id(p2)", id(p2))