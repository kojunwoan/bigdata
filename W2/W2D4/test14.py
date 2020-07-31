#1부터 50 사이의 홀수를 리스트로 만들어 화면에 출력
oddN = list(range(1,50,2))
for i in oddN:
    print(i, end=" ")
print()


k = [3,6,9,12,15,18]
#리스트임
for i in enumerate(k):
    print(i)
#k[index] enumerate -> 튜플반환 (인덱스 번호, 컬렉션의 엘리먼트)


m = []
m.append(100)
m.append(200)
print(m)


#n 리스트에 500, 300 두개 추가
n = []
n.append(500)
n.append(300)
print(n)


l = n+m #리스트끼리 합치는 연산.
print(l[-1]) #인덱스 뒤에서 찾기 가능

print(list("닭백숙"))

#민증번호 나눠버리기
personal = list("930531-1234567")
for y in personal[0:2]:
    print(y, end="")
print("년",end=" ")
for m in personal[2:4]:
    print(m, end="")
print("월",end=" ")
for d in personal[4:6]:
    print(d, end="")
print("일")

#슬라이싱 해보기
t = "동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세".split(" ")
t2 = list(t[-4:]) #-4번부터 끝까지

print(t2)
for v in t2:
    print(v)
print(t[:]) #처음부터끝까지 
print(t[::2]) #처음부터끝까지 2개마다
print(t[::-1]) #뒤에서부터


a=[3,0,1,8,7,2,5,4,6,9]
a.sort()
print(a)
a.reverse()
print(a)

k = list(range(1,101))  #1부터 100까지의 값을 요소로 갖는 k리스트 작성
v = list(k[25:45]) # 25~ 45번까지 요소를 잘라와 v리스트 생성
for i in v[::2]: # 반복문 사용하여 홀수번째 요소만 출력
    print(i)