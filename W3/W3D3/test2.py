def factorial(n):
    value = 1
    for i in range(n,1,-1):
        value = value*i
    print(str(n)+"!= ",value)
    return value


x = factorial(3)
y = factorial(5)

def factorial2(n):
    '''
    설명을 써봅시다.
    '''
    value = 1
    for i in range(n,0,-1):
        value = value*i
        if i >= 2:
            print(i,"*", end=" ")
        else:
            print(i," = ", end=" ")
    print(value)

factorial2(7)

print(factorial2.__doc__)

fac = [1,2]
def factorial3(n):
    if len(fac)<n:
        fac.append(factorial3(n-1)*n)
    return fac[n-1]

print(factorial3(5))