from test9 import Animal
class Whale(Animal):
    def __init__(self):
        print("고래 초기화")
        self.species = "흰수염고래"
        self.name = "힁부지"

    def swimming(self):
        print("수영중..")

    def breathing(self):
        print("숨쉬고 살자...")

if __name__=="__main__":
    w = Whale()
    w.swimming()
    w.breathing()