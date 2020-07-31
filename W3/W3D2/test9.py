def printStar(num): #def 함수명(매개변수)
    for i in range(1,num+1):
        print("*"*i)
#    return 반환값

def multiplication(num):
    for i in range(1,10):
        print("{} * {} = {}".format(num,i,num*i),end='\t')
    print()
#1부터 지정한 숫자까지 누적된 값을 출력하는 함수
def sum_(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    print(sum)
    return sum

printStar(2)
printStar(5)
printStar(10)
multiplication(2)
multiplication(7)
multiplication(9)
print(sum_(100))

def odd(num,step):
    sum = 0
    for i in range(0,num,step):
        sum += i
    return sum
a=odd(100,5)
b=odd(30,3)
print(a,b)