#주사위 합4
for i in range(1,7):
    for j in range(1,7):
        if i+j==4:
            print("({},{})".format(i,j))

#윤년
year = int(input("연도 입력 : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,"년은 윤년입니다.")
else:
    print(year,"년은 윤년이 아닙니다.")

#hap minus multi div
def hap(num1,num2):
    return num1 + num2
def minus(num1,num2):
    return num1 - num2
def multi(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 // num2

print(hap(100,200))
print(minus(200,100))
print(multi(200,3))
print(div(200,3))


#3*3행렬 덧셈
a = [[3,2,3],[4,5,6],[1,4,9]]
b = [[1,8,7],[6,4,4],[3,2,3]]
c = []
for i in range(3):
    d = []
    for j in range(3):
        d.append(a[i][j]+b[i][j])
    c.append(d)
print(c)

#5*5행렬 만들기
a = []
for i in range(5):
    b = []
    for j in range(5):
        b.append(j+1+i*5)
    a.append(b)
print(a)

#학생 10명 성적 총점 평균
st = []
for i in range(1,11):
    st.append(int(input("{}번째 학생 성적 : ".format(i))))
sum = 0
for i in st:
    sum += i
print("총점 : {}\t평균 : {}".format(sum, sum/len(st)))

#100까지 정수 리스트
a = []
for i in range(1,101):
    a.append(i)
print(a)

#위에꺼 코드 + 3333 5555 3535 대입
a = []
for i in range(1,101):
    if i%3==0 and i%5==0:
        a.append(3535)
    elif i%3==0:
        a.append(3333)
    elif i%5==0:
        a.append(5555)
    else:
        a.append(i)
print(a)


#정수 10개 리스트 3의배수 출력
import random
a = []
for i in range(10):
    a.append(random.randint(1,1000))
    if a[i]%3==0:
        print(a[i],end='\t')