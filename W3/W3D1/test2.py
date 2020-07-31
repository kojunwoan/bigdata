import random
#라이브러리 불러오기

# for i in range(10):
#     print(random.random())  #0~1 float

#for i in range(1,101):
#    print(random.randint(1,6), end=" ")  #1~6 int

m = list(range(1,46))       #순서O, 중복O
for l in range(int(input("추첨횟수?"))):
    for i in range(1000):
        a, b = random.randint(0,len(m)-1), random.randint(0,len(m)-1)
        m[a], m[b] = m[b], m[a]
    n = []
    for j in range(6):
        n.append(m[j])
    n.sort()
    print("----------------로또번호 추첨기(",l+1,")번째----------------")
    for k in n:
        print(k,end="\t")
    print(m[6])
