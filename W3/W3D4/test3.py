# map() built-in 함수, list나 dictionary와 같은 iterable한 데이터를 인자로 받아 list안에 개별 item을 함수의 인자로 전달하여 
# 결과를 list형태로 주는 함수

def func1(x):
    return x*2

m = [10,20,30,40]

n = []
for i in m:
    n.append(func1(i))
print(n)
print(list(map(func1,m)))

t = {1:100 , 2:200, 3:300}
print(list(map(func1,[t[i] for i in t])))

def makeString(x):
    if x%3 == 0:
        return str(x)
    else:
        return x

a = [i for i in range(1,11)]
print([i for i in a if i%3==0])
print(list(map(makeString,[i for i in a if i%3==0])))
print(list(map(makeString,a)))
print(list(map(lambda x : str(x) if x%3==0 else x,a)))

def primeNumber(x):
    pn = True
    for i in range(2,x//2):
        if x%i == 0:
            pn = False
            break
    if pn:
        return float(x)
    else:
        return x



#filter : 조건에 일치하는 값만 추출할 때 사용하는 함수
def test2(x):
    if x>0:
        return x
    else:
        return None

n = [-3,-2,-1,0,1,2,3]

print(list(filter(test2,n)))
print(list(filter(lambda x : x>0 ,n)))

# 60~90 탈락
score = [80,70,53,90,70,80,49,99]
def test3(x):
    if 60 <= x <= 90:
        return x
print(list(filter(lambda x : x >= 60,score)))
print(list(filter(lambda x : 70 <= x <=90,score)))




#현재 작업디렉토리에서 파일들의 목록 가져와
#png 파일의 확장자만 검사해서 파일의 이름 출력
file_names = ['movie1.jpg','movie2.png','rabbit.png','bg.png','test.txt','test2.py']
# for i in file_names:
#     if i.find('.png') != -1:
#         print(i)
# png_file = [i for i in file_names if i.find('.png')!=-1]
print(list(filter(lambda i : i.find('.png')!=-1,file_names)))
#맵 -> 모든값들의 결과를 명시 // 필터 -> 조건에 만족하는 값들만 가져옴







sosu = [2]
def addSosu(x):
    for i in range(3,x+1):
        for j in sosu:
            if(i%j==0):
                break
            elif(j>i//2):
                sosu.append(i)
                break

def primeNumber1(x):
    if x not in sosu:
        addSosu(x)
    if x in sosu:
        return float(x)
    else:
        return x
print(primeNumber1(19997))
print(sosu)