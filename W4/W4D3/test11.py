#부모를 만들고 자식을 만들었음 -> 구체화
from test10 import Parent
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.score = 400
        self.name = "홍길동"
        self.age = 20

    def goClub(self):
        print("움칫둠칫 레츠 파뤼타임")
#메소드 오버라이딩
    def singing(self):
        print("루룰루룰루루루루룰ㄹ루룰")
    

if __name__=="__main__":
    c = Child()
    print(c.name, c.age, c.country)
    c.eating()
    c.sleeping()
    c.singing()
    c.cooking()