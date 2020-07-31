def add(a,b):
    '''
    두수의 합을 리턴
    '''
    return a+b

def minus(a,b):
    '''
    두수의 차를 리턴
    '''
    return a-b

def add_minus(a,b):
    return a+b, a-b

# help(add(200,100))
# help(minus(200,100))
print(add_minus(200,100))
x, y = add_minus(200,100)   #언패킹
print(x,y)

#언패킹
i, j = (1, 2)   #튜플
i, j = 1, 2     #튜플(괄호 생략 가능)
i, j = [1, 2]

#함수의 리턴값 : 정수,문자,실수,튜플,리스트........
def hap(a,*b):      #가변인수
    v = a
    for i in b:
        v += i
    return v
print(hap(100,200))
print(hap(100,200,300))