# has a 관계
# 자동차 -- 엔진

class Engine:
    def __init__(self):
        print("카봇 엔진입니다.")

    def start(self):
        print("엔진 동작하는중..")

class Car:
    def __init__(self):
        print("카봇")
        self.Engine = Engine()
        print("엔진 장착")
    def run(self):
        self.Engine.start()

c = Car()
c.run()