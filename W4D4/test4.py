class Gun:
    def __init__(self,name,bullet):
        self.name = name
        self.bullet = bullet

    def fire(self):
        if self.bullet:
            self.bullet -= 1
            print("빵야!! ({}발 남았습니다.)".format(self.bullet))
        else:
            print("틱!")

    def reload(self):
        print("찰카닥")
        self.bullet=20
# g = Gun("AK47", 20)

# for i in range(30):
#     g.fire()
# g.reload()
# g.fire()

class Police(Gun):
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.gun = None

    def receive_gun(self,gun):
        self.gun = gun

    def patrol(self):
        print("순찰중........") 

    def arrest(self,who):
        print(who,"를 체포합니다.")

    def notify_miranda_rights(self):
        print("당신은 묵비권을......") 

    def eat_donut(self):
        print("냠냠")

    def use_weapon(self):
        if self.gun != None:
            self.gun.fire()
        else:
            print("없네....")

g = Gun("k5",12)
p = Police("까오","형사") 
p.use_weapon()
p.receive_gun(g)
p.use_weapon()
p.gun.reload()