#학점 출력 프로그램
kr, en, ma = input("국어, 영어, 수학 점수를 입력하시오(구분자' '): ").split(" ")
kr, en ,ma = int(kr), int(en), int(ma)

total = kr+en+ma
avg = total/3
if avg >= 90:
    print(avg, "점 : A")
elif avg >= 80:
    print(avg, "점 : B")
elif avg >= 70:
    print(avg, "점 : C")
elif avg >= 60:
    print(avg, "점 : D")
else:
    print(avg, "점 : F")