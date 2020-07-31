a = 10              #전역변수
def prt():
#     a = 20          #지역변수
#     print(a)
    global a        #전역변수 쓰기 위해..
    a = 30
    print(a)
    b=100
    print(b)
    print(locals()) #지역변수 뭐있나 확인하기
 
prt()
print(locals())
print(a)
