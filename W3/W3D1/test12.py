import random

# while True:
#     value = int(input("숫자를 입력하세요 : "))
#     #5의 배수인가요?
#     if value % 5 == 0:
#         print(value,"는 5의 배수입니다.")
#         continue
#     print(value,"는 5의 배수가 아닙니다.")
#     break
# print("이제 그만")


#1부터 100까지 수중 3의 배수 5개만 출력
num = []
cnt = 0
while True:
    a = random.randint(1,100)
    if a % 3 == 0:
        if len(num)>0:
            for i in num:
                if i == a:
                    break
                if i == num[len(num)-1]:
                    cnt += 1
                    num.append(a)
        else:
            cnt += 1
            num.append(a)
    if cnt == 5:
        print(num)
        break