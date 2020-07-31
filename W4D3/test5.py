from test9 import Animal            #자식을 만들고 부모를 만들었음 -> 추상화
class Monkey(Animal):
    def __init__(self):
        print("원숭이 초기화")
        super().__init__()      #부모에게서 상속받은 변수들 사용하기.
        self.hand = 2
        self.species = "알락꼬리여우원숭이"
        self.name = "파이숭이"

    def climing(self):
        print("나무를 탑니다.")

    def jump(self):
        print("뜁니다")

if __name__=="__main__":
    m = Monkey()
    m.climing()
    m.jump()
    print(m.eyes)