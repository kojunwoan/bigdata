#부모를 만들고 자식을 만들었음 -> 구체화
class Parent:
    def __init__(self):
        self.name = "홍판서"
        self.age = 60
        self.height = 160
        self.gender = "남"
        self.country = "조선"

    def eating(self):
        print("머거머거")

    def sleeping(self):
        print("쿠울쿨 Zz")

    def singing(self):
        print("뽕짝 뽕짝 뽕짜짝 뽕짝")

    def cooking(self):
        print("팟팟팟팟팟팟")

if __name__=="__main__":
    p = Parent()
    print(p.name, p.age, p.country)
    p.eating()
    p.sleeping()
    p.singing()
    p.cooking()