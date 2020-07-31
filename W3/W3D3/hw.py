#암호화 복호화
def setEncryption():
    for i in input("암호화 할 메세지를 입력하시오.\n"):
        i = ord(i)
        if 65 <= i <= 87 or 97 <= i <= 119:
            i += 3
        elif 88 <= i <= 90 or 120 <= i <= 122:
            i -= 23
        print(chr(i),end="")

def getDecode():
    for i in input("복호화 할 메세지를 입력하시오.\n"):
        i = ord(i)
        if 68 <= i <= 90 or 100 <= i <= 122:
            i -= 3
        elif 65 <= i <= 67 or 97 <= i <= 99:
            i += 23
        print(chr(i),end="")

if int(input("1.암호화\t2.복호화\n"))-1:
    getDecode()
else:
    setEncryption()
print()

#스코어 출력
score = [
	[80,80,80,0,0],
	[60,50,80,0,0],
	[50,90,90,0,0],
	[40,50,60,0,0],
	[90,90,95,0,0],
	[85,95,100,0,0]]
    
for i in score:
    i[3]=i[0]+i[1]+i[2]
    i[4]=i[3]/3
print(score)


#baseball
import random
v = set()
while len(v)<3:
    v.add(str(random.randint(0,9)))
    if list(v)[0]==0:
        v.remove(0)
v = tuple(v)

count = strike = 0
while strike!=3:
    num , count = input("입력 : "), count+1
    print(v,num)
    strike = ball = 0
    for idx,val in enumerate(num):
        if val in v:
            if val == v[idx]:
                strike += 1
            else:
                ball += 1
    msg = ""
    if strike:
        msg += "{}S".format(strike)
    if ball:
        msg += "{}B".format(ball)
    if not(ball or strike):
        msg += "out"
    print("출력 : "+msg)
print("3STRIKE!!! {}회만에 성공하셨습니다.".format(count))

#
def printGuGuDan(st,en):
    for i in range(st,en+1):
        for j in range(1,10):
            print("{} * {} = {}".format(i,j,i*j))
        print("-------------------")