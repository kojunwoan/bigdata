#가위 바위 보
import random

v = ["가위","바위","보"]
while True:
    r = random.randint(0,2)
    p = input("가위 바위 보! ")
    for i in range(3):
        if v[i] == p:
            p=i
    if p-r == 0:
        print(v[p], "vs", v[r], "비김")
    elif p-r == 1 or p-r == -2:
        print(v[p], "vs", v[r], "승리!!")
    elif p-r == -1 or p-r == 2:
        print(v[p], "vs", v[r], "패배 ㅠㅜ")
    else:
        print("값을 잘못 입력했습니다.")