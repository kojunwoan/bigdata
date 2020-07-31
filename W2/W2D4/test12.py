#문자열
name = 'my name is "KS"'
print(name)
sorry = "i am sorry"
sorry = "i'm sorry"

hobby = "cyber \n fishing"
print(hobby)

a,b,c,d,e=10,20,30,40,50

print(a,b,c,d,e)

#리스트 : 대괄호로 묶어준다. 각각의 값을 element로 구분 구분은 ,로 한다.
a = [10,20,30,40,50]
print(a)
print(a[0])
#초기선언
m = []
#연속된 값 만들기
print(range(10))
m = list(range(0,10))

print(m)
k = list(range(20,10,-3))
print(k)

#3의배수 출력
print(list(range(3,1000,3)))

#달의 표면은 밤 : -170 낮 120도 , 3도씩 상승한다고 가정
print(list(range(-170,120,3)))