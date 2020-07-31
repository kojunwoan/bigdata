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