# 함수를 호출할때 다시 꺼내서 사용하는 함수 : 클로저(closure)

def plus_ten1():
    a = 10
    def add(b):
        return a+b
    return add      #add함수를 사용하기 전까지 메모리에서 제거되지 않음.

cal = plus_ten1()

print(cal(10))

def plus_ten2():
    a = 10
    return lambda b : a+b

cal2 = plus_ten2()

print(cal2(100),cal2(200))