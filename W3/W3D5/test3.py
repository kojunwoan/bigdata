#nested function (중첩 함수)
def sayHello():
    msg = "니하오"          #prt함수에서는 전역변수처럼 사용함
    def prt():
        print(msg)          #중첩함수에서는 이전단 함수의 변수 사용 가능
    prt()

sayHello()


def f1():
    a = 10
    def f2():
        nonlocal a          #f1의 지역변수 사용
        a = 20
    f2()
    print(a)

f1()        