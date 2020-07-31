# set: 순서X, 중복X
a={1,2,3,1}
b={3,4}
print(a,type(a))
#print(a[0]) 순서가 없어서 뽑아올 수 없음.

print(a.union(b), a|b, a.intersection(b), a&b, a-b)   #합집합, 교집합, 차집합

b.add(5)            #한가지 값 추가 할때
b.update({6,7})     #set으로 추가 
b.update((8,9))     #튜플로 추가
b.update([10,11])   #리스트로 추가
print(b)

#삭제 방식 2가지
b.discard(7)
b.remove(8)
print(b)

print("------------------")
c=set()
c=b
print(c)
c.clear()   #전체 제거
print(c)

#중복된 값을 제거하고 정렬
m = [2,3,11,29,3,2,7,8,11]
m = list(set(m))        #set으로 만들어 중복값을 제거하고 
m.sort()
print(m)