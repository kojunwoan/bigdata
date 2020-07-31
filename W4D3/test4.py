from test9 import Animal
class Rabbit(Animal):
    def __init__(self):
        print("토끼 초기화")
        self.species = "앙골라"
        self.name = "토순이"

    def jump(self):
        print("깡총")

if __name__=="__main__":
    r = Rabbit()
    r.jump()
    r.eating()
    r.sleeping()