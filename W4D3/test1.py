class Test:
    def __init__(self,balance):
        self.balance = balance

    def print(self):
        print("잔액 :" , self.balance)


t = Test(5000)
t.aaa = 200 #없을때 생성 가능
t.print()
print(t.aaa)
print(t)