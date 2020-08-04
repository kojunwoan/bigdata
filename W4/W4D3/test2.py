
class ATM:
    def __init__(self):
        self._acc = "110"       #클래스안에서만 사용 가능
        self.__balance = 0       #클래스안에서만 사용 가능
        self.name = "홍길동"
        print("초기화", self.name, self.__balance)
        
    def set_balance(self,balance):
        self.__balance = balance
        
    def get_balance(self,balance):
        print("현재 잔액 :",self.__balance)

    def deposit(self, money):
        self.__balance += money
        print(money, "원 입금합니다.")
        print("현재 잔액 :",self.__balance)

    def withDraw(self,money):
        if self.__balance >= money:
            self.__balance -= money
            print(money, "원 출금합니다.")
        else:
            print("잔액이 {}원보다 적습니다.".format(money))
        print("현재 잔액 :",self.__balance)

auto = ATM()
print(auto)

auto.deposit(100000)
auto.deposit(100000)
auto._acc = "357"       #_ 내부변수로 생각하도록 사용(암묵적 사용)
# print(auto.__balance) #__ 무조건 내부변수로 사용(강제적 사용)    
auto.__acc= "010"       #__acc 새로만든 변수명일뿐 강제기능 없음
print(auto.__acc)       #밖에서 사용 잘됨ㅋ
auto.set_balance(5000)  #인스턴스 함수로 만들어서 내부에서 변경하도록 함
auto.withDraw(800000)