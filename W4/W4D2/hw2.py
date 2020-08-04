class GuGuDan:
    def __init__(self):
        self.dan = 0
    
    def print(self):
        for i in range(1,10):
            print("{} * {} = {}".format(self.dan,i,self.dan*i))

g = GuGuDan()
g.dan = 3
g.print()

class TV:
    def __init__(self):
        self.power = False
        self.channel = 1
    def turnOnOff(self):
        if self.power:
            self.power = False
        else:
            self.power = True
    def changeChannel(self,n):
        self.channel = n

class HandPhone:
    def __init__(self):
        self.phone_number = '011-1111-2222'
        self.internet = False

    def call(self,n):
        print("{}에서 {}번으로 전화거는중".format(self.phone_number, n))

    def connect_internet(self):
        self.internet = True
        print("인터넷에 연결되었습니다.")


hp = HandPhone()
hp.call("011-1234-5678")  #011-1111-2222에서  011-1234-5678번으로 전화거는중 
hp.phone_number= "010-1234-5678" # 011-1111-2222 에서 전화번호를 010-1234-5678 로변경함 
hp.call("011-1234-5678")  #010-1234-5678에서  011-1234-5678번으로 전화거는중 
hp.connect_internet() # 인터넷에 연결되었습니다. 

