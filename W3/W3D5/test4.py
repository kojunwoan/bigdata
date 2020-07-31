#파이썬의 함수는 모두 일급 함수
#함수를 다른 함수의 인수로 전달할 수 있다.
#함수의 반환값으로 함수를 사용 할 수 있다.
#변수나 자료구조에 저장할 수 있다.

def add(a,b):
    return a+b


plus = add
print(plus(500,400))

def appendFunction(f1,c,d):
    return f1(c,d)

print(appendFunction(add,300,200))
