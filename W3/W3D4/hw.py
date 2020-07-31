#1
#소문자 대문자 숫자 가능/특수문자(_제외) 불가능/ 첫글자 숫자불가능 _가능 / 예약어 불가능/ 의미있게 == 알아보기 쉽게

#2
def square(x):                                  #제곱으로 반환해주는 함수
    return x*x
print(square(5))                                #5->25

#3
print((lambda x : x*x)(5))                      #람다를 이용해 제곱반환 함수 사용

#4
m = [i for i in range(1,101)]                   #1~100까지 담긴 리스트m
def triple(x):                                  #3배로 반환해주는 함수triple
    return x*3
print(list(map(triple,m)))                      #리스트m을 triple함수에 전부 매핑시키고 리스트화 하여 출력

#5
print(list(map(lambda i : i*3,m)))              #람다를 이용해 3배반환 함수를 만들어 리스트m에 매핑

#6
import random                                   
rnd = set()                                     #set을 만듬(특징: 중복불가)
while len(rnd)<10:                              #set에 값이 10개가 될때까지
    rnd.add(random.randint(1,100))              #1~100중 랜덤값을 추가
rnd = list(rnd)                                 #완성된 set을 list로 형변환
print(min(rnd),max(rnd))                        #내장함수 min과 max를 활용

rnd = []                                        #빈 리스트를 만듬
while len(rnd)<10:                              #리스트에 값이 10개가 될때까지
    a = random.randint(1,100)                   #1~100중 랜덤값을 생성하여
    if a in rnd:                                #그 값이 리스트에 존재하는지 확인하여
        continue                                #있다면 다음 회차를 진행하고
    rnd.append(a)                               #없다면 리스트에 값을 추가
print(min(rnd),max(rnd))                        #내장함수 min과 max를 활용

#7
k = list(range(1,101))                          #1~100값을 순서대로 가진 리스트 생성
print(k)                                        

#8
k = [i for i in range(1,101)]                   #리스트 내포를 활용하여 같은 결과값 생성
print(k)

#9
k = [i for i in range(1,101) if i%2==0]         #리스트 내포를 활용하여 짝수만 생성
print(k)