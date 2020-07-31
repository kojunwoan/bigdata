import random
from math import pi
class Agar:
    def __init__(self,nickname,color):
        self.radius = 5
        self.color = color
        self.nickname = nickname
        self.x = random.randint(1,100)
        self.y = random.randint(1,100)
        self.weight = 10

    def feeding(self, other):
        if other.weight < self.weight:
            self.weight += other.weight
        else:
            self.weight += 17
            print("먹이주기")

    def move(self):
        print("이동하기")

    def split(self):
        self.weight = self.weight//2
        self.radius = self.radius//2
        print("반토막나기")

    def merge(self):
        self.weight += 1
        self.radius += 0.2
        print("줍줍")
    
    @staticmethod   #@xxxx 데코레이터 static메소드 -> 인스턴스가 없더라도 독립적 사용 가능
    def getArea(radius):
        return radius**2*pi

print(Agar.getArea(50))
a1 = Agar("성은이당",'red')
a1.move()
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
a1.split()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()
print(a1.getArea(a1.radius))
a1.merge()