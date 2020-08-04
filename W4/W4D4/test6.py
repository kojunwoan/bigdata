class Player:
    def __init__(self,name):
        self.hp = 100
        self.name = name
        self.weapon = None

    def receive_weapon(self,weapon):
        self.weapon = weapon
    def use_weapon(self,other):
        self.weapon.use(other)

class Weapon:
    def __init__(self):
        pass
    def use(self):
        pass
    def reuse(self):
        pass

class Gun:
    def __init__(self,name,bullet,dam):
        self.name = name
        self.maxbullet = bullet
        self.bullet = bullet
        self.dam = dam
    def use(self,other):
        self.fire(other)
    def fire(self,other):
        print("빵야 으악")
        other.hp -= self.dam
    def reload(self):
        self.bullet = self.maxbullet

class Knife:
    def __init__(self,name,dam):
        self.name = name
        self.dam = dam
    def use(self,other):
        self.swing(other)
    def swing(self,other):
        print("휙 푹찍")
        other.hp -= self.dam

class Grenade:
    def __init__(self,name,dam):
        self.name = name
        self.dam = dam
    def use(self,other):
        self.throw(other)
    def throw(self,other):
        print("휘잉~~~~ 펑")
        other.hp -= self.dam

p1 = Player("ㅁㅈㅇ")
p2 = Player("해피너스")
gu = Gun("k5",12,30)
kn = Knife("장미칼",20)
gr = Grenade("연습용수류탄",1)
p1.receive_weapon(gu)
p1.use_weapon(p2)
p1.receive_weapon(kn)
p1.use_weapon(p2)
p1.receive_weapon(gu)
p1.use_weapon(p2)