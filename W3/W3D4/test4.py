#내장함수

print(sum([10,20,30]), sum((10,20)), sum({2,3}))

print(bin(8))
print(int(2.7), float(3), str(5) + '오')

a = 10

b = eval('a + 5')

print(b)

print(round(1.2), round(1.6))   #반올림

import math

print(math.ceil(1.2), math.ceil(1.6))   #올림
print(math.floor(1.2), math.floor(1.6)) #내림

bList = [True, 1, False]

print(all(bList))   #and
print(any(bList))   #or


#재귀호출
def factorial(i):
    if i == 2:
        return 2
    return i*factorial(i-1)

print(factorial(5))

def fibonacci(i):
    if i in [1,2]:
        return 1
    return fibonacci(i-1)+fibonacci(i-2)

def fibonacci1(i):
    fibList=[0,1]
    for j in range(1,i):
        fibList.append(fibList[j]+fibList[j-1])
    print(fibList)
    return fibList[i]
print(fibonacci(5))
print(fibonacci1(5))
