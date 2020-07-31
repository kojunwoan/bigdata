#랜덤하게 10개 숫자 생성(1~999)
#이것을 리스트에 담는다.
#최대값을 구해서 출력
import random
num = []
for i in range(10):
    num.append(random.randint(1,999))
print(min(num),max(num))

min = max = num[0]
for i in num:
    if max < i:
        max = i
    if min > i:
        min = i
print(min ,max)
