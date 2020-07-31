mList = [1000,2000,3000,4000,5000]
#List comprehension(리스트 내포)
mList = [int(i * 1.1) for i in mList]
print(mList)


list2 = [-5,-2,-1,0,2,-3,-2,10,3]
print([[idx,val] for idx,val in enumerate(list2) if val>=0])

#람다 함수(익명함수)
#이름이 없는 함수
#코드가 간결, 메모리의 절약
def test(x,y):
    return x+y
print(test(100,200))
lambda x : x+1
print((lambda x,y : x+y)(100,200))        #선언불필요하고 바로 만들고 값써서 끝

ts = test
print(type(test),id(test))
print(type(ts),id(ts))

lmadd = lambda x,y : x+y
print(lmadd(100,200))

#조건식을 사용한 람다
print((lambda a,b : a if a%2==0 else b)(19,15))