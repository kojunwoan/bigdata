#제어문
#조건 분기문
#주어진 조건 발생하면 다른 문장이 실행되게 처리

#사용자로부터 성적 입력 받기

score = int(input("당신의 성적을 입력받으세요."))

prt = ""
con = ""
if score>=90:
    prt = "A"
    con = "\n축하합니다. 짝짝짝"
elif score>=80:
    prt = "B"
elif score>=70:
    prt = "C"
elif score>=60:
    prt = "D"
else:
    prt = "F"
print(score,"점은 "+prt+"학점입니다."+con)


#1부터 20까지 홀수 값을 출력
for i in range(1,21):
    if i%2==1:
        print(i,end="")
print()

for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",end="")
        if j%2 == 1:
            print(i*j)
        else:
            print("****")
