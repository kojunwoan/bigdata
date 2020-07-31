# 1. 클래스, 객체, 인스턴스? 
#클래스     : 일정한 특징을 가진 사물들을 만들어 낼 수 있는 설계도
#객체       : 사물
#인스턴스   : 프로그램상에서 만든 사물


# # 2.  아무것도 없는  Cat 클래스를 정의하세요 
# class Cat:
#     pass
class Cat:
    def __init__(self,name="고양이",age=1):
        self.name = name
        self.age = age
        print("야옹야옹")

    def __str__(self):
        return "이름 : "+self.name+" , 나이 : "+str(self.age)
    
    def __del__(self):
        print("고양이 죽는다 야옹")

    def play(self,what):
        print(what+"을 가지고 놀고 있다냐옹")

    def info(self):
        print("이름 : {} , 나이 : {}".format(self.name, self.age))

    def eat(self,what):
        print("나비가 {}을 먹고 있어요".format(what))
# 3.  다음 코드로 야옹야옹 이라는 메세지를 출력하도록 Cat 클래스를 수정하세요 
#      nabi = Cat()
# #      야옹야옹  
nabi = Cat()
# 4. 
#       nabi.play("공")
# #      공을 가지고 놀고 있다냐옹 
nabi.play("공")
# 5.   생성자 추가 
#      nabi2 = Cat("나비", 2)
nabi2 = Cat("나비", 2)
# 6.
#     print(nabi2)
#     이름 : 나비 , 나이 : 2 
print(nabi2)
# 7. 
#      nabi2.info()
#     이름 : 나비 , 나이 : 2 
nabi2.info()
# 8.
#      nabi2.eat("생선")
#      나비가 생선을 먹고 있어요 
nabi2.eat("생선")
# 9.
#      del  nabi2 
#      고양이 죽는다 야옹 
del nabi2 
# 10.  Customer 인스턴스를 생성할수 있도록 클래스를 정의하세요 
#       c =   Customer ("홍길동", 20, "990101-1234567")
class Customer:
    deposit_count = 0
    def __init__(self,name,age,ssn):
        self.name = name
        self.age = age
        self.ssn = ssn
        self.__balance = 0
    def __del__(self):
        print("그 동안 이용해주셔서 감사합니다.\n계좌 잔액 : {}".format(self.__balance))

    def show(self):
        print("{}님 현재 잔액은 {}원 입니다.".format(self.name, self.__balance))
    def deposit(self,money):
        self.__balance += money
        print("{}님 계좌에 {}원 입급합니다.".format(self.name, money))
        self.show()
        self.deposit_count += 1
        if self.deposit_count % 5 == 0:
            self.interest()
    def withDraw(self,money):
        if self.__balance >= money:
            self.__balance -= money
            print("{}님 계좌에서 {}원 출금합니다.".format(self.name, money))
            self.show()
        else:
            print("잔액이 부족합니다.")
            self.show()
    def get_balance(self):
        return "잔액값 가져오기 : {}".format(self.__balance)
    def set_balance(self,money):
        self.__balance = money
        print("잔액을 {}으로 변경".format(money))
    def interest(self):
        self.__balance *= 1.05
        print("이자 발생")
        self.show()
c = Customer ("홍길동", 20, "990101-1234567")
# 11. 
#       c.show()
#      # 홍길동님 현재 잔액은 0원입니다. 
c.show()
# 12. 
#        c.deposit(5000)
#      # 홍길동님 계좌에 5000원 입금합니다.
#      # 홍길동님 현재 잔액은 5000원입니다. 
c.deposit(5000)
# 13.
#        c.withDraw(9000)
#     # 잔액이 부족합니다. 
#      # 홍길동님 현재 잔액은 5000원입니다. 
c.withDraw(9000)
# 14.
#     c.withDraw(2000)
#     # 홍길동님 계좌에 2000원 출금합니다.
#      # 홍길동님 현재 잔액은 3000원입니다. 
c.withDraw(2000)
# 15.
#        Customer 클래스에 인스턴스 속성의 값을 을 수정할수 있는 setter, getter 
# 	클 추가합니다. 
#       print(c.get_balance()) # 잔액값 가져오기 : 3000
#       c.set_balance(30000) # 잔액을 30000으로 변경 
print(c.get_balance())
c.set_balance(30000)
# 16.
# 	5회 입금할때마다 
# 	잔액의 5%씩 이자 발생 
c.deposit(1000)  #   31000
c.deposit(3000)  #   34000
c.deposit(2000)  #   36000
c.deposit(2000)  #   38000
c.deposit(3000)  #   41000
# 	# 이자발생   # 43050

# 17.
# 	del c 
# 	# 그 동안 이용해주셔서 감사합니다 
# 	# 계좌 잔액 : 43050 
del c 


