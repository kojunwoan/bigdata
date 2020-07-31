def make1(fn):
    return (lambda : "니하오 " + fn())

def make2(fn):
    return (lambda : "알로하 " + fn())

def hello():
    return "한라봉"

print(make1(hello)())

hi = make2(make1(hello))
print(hi())

'''
print(hi())
print(make2(make1(hello))())            make2(fn) => fn = make1(hello)
print((lambda : "알로하 " + make1(hello)())())      make1(fn) => fn = hello
print((lambda : "알로하 " + (lambda : "니하오 " + hello())())())
print((lambda : "알로하 " + (lambda : "니하오 " + "한라봉")())())
print((lambda : "알로하 " + "니하오 한라봉")())
print("알로하 니하오 한라봉")
'''

def make3():
    return lambda : "니하오"
print(make3()())

#데코레이터(decorator)
@make2
@make1
def hello2():
    return "소망이"

print(hello2())