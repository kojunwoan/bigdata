class card():
    def __init__(self, name, rarity, cost, atkpoint, hp):
        self.name = name
        self.rarity = rarity
        self.cost = cost
        self.atkpoint = atkpoint
        self.hp = hp
        print("초기화 완료")

    def attack(self, other):

        other.hp -= self.atkpoint
        self.hp -= other.atkpoint
        print("{}의 체력이 {}입니다.".format(self.name, self.hp))
        print("{}의 체력이 {}입니다.".format(other.name, other.hp))

card1 = card("돌엄니 멧돼지",0,1,1,1)
card2 = card("멀록 약탈꾼",0,1,2,1)

card1.attack(card2)



class Marine:
    def __init__(self):
        self.maxhp = 40
        self.hp = 40
        self.attackPoint = 6
        self.attackSpeed = 15

    def attack(self,other):
        if other.hp > 6:
            other.hp -= self.attackPoint
        else:
            print("고마해라.. 마이 무긋따 아이가?")
        print("체력이 %d상태입니다."%other.hp)

    def move(self):
        print("GoGoGo")

    def steamPack(self):
        if self.hp > 10:
            self.hp -= 10
            self.attackSpeed = 9
            print("스팀팩 사용!")
            from time import sleep
            sleep(13.5)
            self.attackSpeed = 15
            print("스팀팩 끝!")
        else:
            print("체력이 부족합니다.")

m1 = Marine()
m2 = Marine()

for i in range(10):
    m1.attack(m2)
print(m2.hp)
# m1.steamPack()

class Medic():
    def __init__(self):
        self.maxhp = 60
        self.hp = 60
        self.mp = 200
        self.healPower = 11.72
        self.defense = 1
        self.x = 100
        self.y = 100

    def heal(self, other):
        from time import sleep
        while other.hp < other.maxhp:
            print("체력이 {}에서".format(int(other.hp)),end=" ")
            other.hp += self.healPower
            if other.hp > other.maxhp:
                other.hp = other.maxhp
            print("{}로 변했습니다.".format(int(other.hp)))
            self.mp -= 5.86
            sleep(1)

me1 = Medic()
me1.heal(m2)