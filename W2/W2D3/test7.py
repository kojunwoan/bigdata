#숫자형 변수
#정수 (integer)
#실수 (float)
#복소수 (complex) ex) 1.9j

a=10.1j
print(type(a))
a=10.1
print(type(a))
a=10
print(type(a))
b=10.5
print(type(a+b))
c="20"
print("c = " + c)
print("a = " + str(a))

a=10.5
b=20
print(type(a),"a : " , a ,"," , type(b),"b :" , b)

temp=a
a=b
b=temp
print(type(a),"a : " , a ,"," , type(b),"b :" , b)

a,b = b,a
x = y = z = 20
i , j = 10, 20
x = None
a = 100 
a += 20
