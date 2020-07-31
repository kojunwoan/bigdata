def show_info(name, job, age, loc, height):
    # pass 에러방지
    print("이름: {}\t직업: {}\t나이: {}\t사는곳: {}\t키: {}\t".format(name,job,age,loc,height))

show_info("홍길동", "도적", 20, "율도국", 180.3)

#이름: 홍길동   직업: 도적  나이:20 사는곳:율도국   키:180.3

p = {'name':'홍길동', 'job':['도적','의적'], 'age':20, 'loc':'율도국', 'height':180.3}
show_info(**p)
# * : key
# ** : value

def test(a,b,c):
    print(a)
    print(b)
    print(c)
#동적타이핑이기 때문에 매개변수 하나씩 지칭하는게 가능함..
test(b=20,a=10,c=30)

x = [10,20,30]
def sumvalue(a,b,c):
    return a+b+c
print(sumvalue(*x))



#가변인수로 함수 만들수 있다.
def sumvalue2(*args):
    print(args)
sumvalue2(x)

def show_info2(**kwargs):
    for kw, arg in kwargs.items():
        print(kw,":",arg,sep='')

show_info2(name="홍길동")
show_info2(**p)

def find_birth(ssn):
    print("{}년 {}월 {}일".format(ssn[0:2],ssn[2:4],ssn[4:6]))

find_birth("880101-1234567")
