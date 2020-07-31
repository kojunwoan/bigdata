from time import sleep

class Marine:
    def __init__(self):
        self.maxhp = 40
        self.hp = 40
        self.attackPoint = 6
        self.attackSpeed = 15
        self.bio = True
        self.mechanic = False

    def attack(self,other):
        if other.hp > self.attackPoint:
            other.hp -= self.attackPoint
        else:
            print("고마해라.. 마이 무긋따 아이가?")
        print("체력이 %d상태입니다."%other.hp)
        sleep(self.attackSpeed/10)

    def move(self):
        print("GoGoGo")

    def steamPack(self):
        if self.hp > 10:
            self.hp -= 10
            self.attackSpeed = 9
            print("스팀팩 사용!")
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

class Medic:
    def __init__(self):
        self.maxhp = 60
        self.hp = 60
        self.maxmp = 200
        self.mp = 50
        self.healPower = 5.86
        self.defense = 1
        self.x = 100
        self.y = 100
        self.bio = True
        self.mechanic = False

    def heal(self, other):
        from time import sleep
        if other.bio:
            while other.hp < other.maxhp:
                print("체력이 {}에서".format(int(other.hp)),end=" ")
                other.hp += self.healPower
                if other.hp > other.maxhp:
                    other.hp = other.maxhp
                print("{}로 변했습니다. mp : {}".format(int(other.hp),self.mp))
                self.mp -= self.healPower/2
                sleep(1)

me1 = Medic()
me1.heal(m2)


class Ghost:
    def __init__(self):
        self.maxhp = 45
        self.hp = 45
        self.attackPoint = 10
        self.attackSpeed = 22
        self.invisible = False
        self.bio = True
        self.mechanic = False

    def Cloaking(self):
        if self.invisible:
            self.invisible = False
        else:
            self.invisible = True
        
    def attack(self,other):
        if other.hp > self.attackPoint:
            other.hp -= self.attackPoint
        else:
            print("고마해라.. 마이 무긋따 아이가?")
        print("체력이 %d상태입니다."%other.hp)
        sleep(self.attackSpeed/10)

        
class SiegeTank:
    def __init__(self):
        self.maxhp = 150
        self.hp = 150
        self.attackPoint = 30
        self.attackSpeed = 37
        self.mode = False
        self.bio = False
        self.mechanic = True

    def SiegeMode(self):
        if self.mode:
            self.mode = False
            self.attackPoint = 30
            self.attackSpeed = 37
        else:
            self.mode = True
            self.attackPoint = 70
            self.attackSpeed = 75

    def attack(self,other):
        if other.hp > self.attackPoint:
            other.hp -= self.attackPoint
        else:
            print("고마해라.. 마이 무긋따 아이가?")
        print("체력이 %d상태입니다."%other.hp)
        sleep(self.attackSpeed/10)

t1 = SiegeTank()
t2 = SiegeTank()
for i in range(5):
    t2.attack(t1)
t1.SiegeMode()
for i in range(5):
    t1.attack(t2)