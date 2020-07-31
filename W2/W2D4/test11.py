print(1+1)
a=10
print(a)

a = float(a)
print(type(a))
print(a)
print(complex(1.3,1.4j))



# x = input("아무 값이나 입력하세요.")
# print("x의 값은 : "+ x)
print(3>5)

a = 100
b = 200
c = None
print(a<b)
print(c)
print(100>2 and 300>100 or 100>200)

X = True
Y = False
print(X and Y)

print(True and True)
print(False or True,end = "\n\n")

a,b = 300 , 200

print(a==b)
print(a!=b)

#국어, 영어, 수학 점수를 입력 받기 평균 60 이상 합격,과락40
kor, eng, mat = input("국어 영어 수학 점수를 입력하시오.").split()
kor, eng, mat = int(kor), int(eng), int(mat)
if (kor>=40 and eng>=40 and mat>=40):
    if((kor+eng+mat)/3>=60):
        print("True(합격)")
    else:
        print("False(불합격)")
else:
    print("False(과락)")

