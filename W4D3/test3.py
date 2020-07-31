class Player:
    #클래스 속성
    cnt = 0
    bag = []

    def __init__ (self,name):
        self.name = name
        self.hp = 1000
        self.attackPoint = 150
        self.cnt +=1

    def put(self, obj):
        Player.bag.append(obj)

    @classmethod
    def getBag(cls):
        print("아이템", cls.bag)

    def attack(self,other):
        
        print(self.name, "이", other.name, "을 공격합니다.", other.hp ,end=" ")
        other.hp -= self.attackPoint
        print("to",other.hp)

    def greeting(self,other):
        print(other.name , "부모님은 잘 계시니??")



p1 = Player("에코")
p2 = Player("야스오")

p1.attack(p2)
print(p1.cnt)
p1.attack(p2)
print(p1.cnt)
p1.attack(p2)
print(p1.cnt)
p2.greeting(p1)

p1.put("권총")
p1.getBag()