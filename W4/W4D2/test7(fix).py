import log

class ATM:
    def __init__(self):
        print("초기화")
        self.balance = 0
        # if log.getBalance("./W4D2/bank.log") > 0:
            # self.balance = 
        log.getBalance("./W4D2/bank.log")
        print(self.balance)
        self.name = "홍길동"
        

    def deposit(self, money):
        self.balance += money
        print(money, "원 입금합니다.")
        print("현재 잔액 :",self.balance)
        log.saveLog("./W4D2/bank.log",money,self.balance,0)

    def withDraw(self,money):
        if self.balance >= money:
            self.balance -= money
            print(money, "원 출금합니다.")
            log.saveLog("./W4D2/bank.log",money,self.balance,1)
        else:
            print("잔액이 {}원보다 적습니다.".format(money))
        print("현재 잔액 :",self.balance)

auto = ATM()
print(auto)

auto.deposit(100000)
auto.deposit(100000)
auto.withDraw(80000)