#튜플 : 리스트와 비슷하지만 한번 생성되면 값을 변경 할 수 없다. / 불변한 순서가 있는 객체의 집합
a = (10,20,30,40,50)
print(a)
b = tuple(range(5,11))
print(b)
print(len(b))
#제어문 : 문장의 흐름을 제어해주는 명령
#for 변수 in 자료형
for i in a:
    print(i)
print("test")

print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")
for i in range(1,21):
    print(i,end =" ")
print("")
for i in range(1,10):
    print("3 *", i ,"=", i*3)

# for i in range(1,10):
d = int(input("몇단?"))
for j in range(1,10):
    print(d,"*",j,"=",d*j)
print()

sum = 0
for i in range(1,int(input("숫자를 입력하시오"))+1):
    sum += i
print(sum)

sosu = [2]
for i in range(3,1001):
    for j in sosu:
        if(i%j==0):
            break
        elif(j>i//2):
            sosu.append(i)
            break
print(sosu)

