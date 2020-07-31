class Animal:
    def __init__(self):
        print("동물 초기화")
        self.eyes = 2
        self.mouth = 1
        self.ears = 2
        self.species = ""
        self.name = ""

    def eating(self,what):
        print(what, "냠냠")
    
    def sleeping(self):
        print(self.name, "쿨쿨")
