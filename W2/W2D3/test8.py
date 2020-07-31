a, b, c = 100, 200, 300
print(a, b, c)
a, b, c = c, a, b
print(a, b, c)
 
a+=10
b+=10
c+=10
print(a, b, c)

a, b = 10, 20
print(a,b) #쉬프트 + 알트 + 화살표 아래 = 복사
print(a-b)
print(a*b)
print(a/b) #실수형
print(a//b)#정수형
print(a%b)

a = -a #음수화

#msg = input("출력할 메세지를 입력하세요.")
#print(msg)

# a = input("a의 값 :")
# b = input("b의 값 :")
# print(int(a)+int(b))

# x = int(input("숫자 입력 하세요."))
# x %= 2
# print(x)

x , y = input("두개의 숫자를 입력하세요").split()
print(x,y)