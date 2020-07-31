#dict : 키 : 값 의 쌍으로 이루어짐 , 순서X
#json : 경량데이터 교환방식

mydic = dict(k1=1,k2="abc",k3=3.4)
print(mydic)

dic = {'파이썬':'뱀','자바':'커피','오라클':'예언자'}
print(dic, len(dic))
print(dic['자바'])
dic['스미스']='백그라운드프로세스'
print(dic)
dic['neo']="키아누 리브스"
dic['스미스']='bg'  #키값은 중복이 안되서 덮어씀
print(dic)
dic['smith']='bg'
print(dic) 
#  print(dic[0])    인덱싱 불가 (순서X)
 # dic.clear()
# print(dic)

for key in dic:
    print(key, dic[key])
for key in dic.values():    #value 만 출력
    print(key)

for key, val in dic.items():    #key와 value 한번에 
    print("key : {}\tval : {}".format(key,val))


print('neo' in dic) #키가 있는지 여부 판단 : in -> boolen
del dic['neo']  #삭제
print(dic)
dic['game']=['대항해시대','바람의나라','문명6','토탈워']
dic['broadcating_co']=['kbs','mbc','sbs','ytn','jtbc']
print(dic)

from pprint import pprint as pp
pp(dic)






print("----------------------------------------------------------------------------")
print("----------------------------------------------------------------------------")

import random
min = 1
max = 100
a = random.randint(min,max)
while True:
    b = (max + min)//2
    if a == b :
        print("{} 와 {} 일치합니다.".format(a,b))
        break
    else:
        if a>b:
            min = b+1
            print(b,"보다 큽니다.")
        else:
            max = b-1
            print(b,"보다 작습니다.")

