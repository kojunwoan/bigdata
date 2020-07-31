a=10
print(a)
print(bin(a))
print(oct(a))
print(hex(a))
print(10,0b1010,0o12,0xa)
print(7+2j,type(7+2j))

b=20
a,b=b,a

a, *b = 1, 2, 3, 4, 5 #리스트 형식으로 여러값 받음
print(a, b)

*a, b, c = 1, 2, 3, 4, 5
print(a, b, c)

print(format(1.2345,'10.3f')) #c
print("나는 나이가 20살 입니다.")
age = 20
print("나는 나이가",age,"살 입니다.")
print("나는 나이가 "+str(age)+"살 입니다.")
print("나는 나이가 %d살 입니다."%20)
print("나는 나이가 %s살 입니다."%'스무')
print("오늘은 %d월 %d일 이고, %s 입니다."%(7,17,'제헌절'))
print("이름은 %s이고, 나이가 %f 입니다."%('뽀로로',20.5))
print("이름은 {0}{0}{0}이고, 나이가 {1} 입니다.".format('뽀로로',20.5))
print("이름은 {1}이고, 나이가 {0} 입니다.".format('뽀로로',20.5))
print("이름은 {}이고, 나이가 {} 입니다.".format('뽀로로',20.5))

#연산자
print(5+3,5-3,5*3,5/3,5//3,5%3,divmod(5,3),5**3)

#부호변경
a=1
print(a,-a,a*-1)

print(bool(0), bool(-1), bool(None), bool(''), bool(True), bool(False))
print('c:\\python\\name\\table')
print('c:/python/name/table')
print(r'c:\python\name\table') #raw data