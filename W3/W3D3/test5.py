#객체 : mutable, immutable
#immutable : bool, int, float, tuple, str : 잘 안바뀌는 애들
#mutable : list, set, dict : id(변수명):해당 변수의 reference(주소)값 나타내는 애들

a = 100
b = a

print(type(a),type(b))
print(id(a),id(b))
#주소(래퍼런스)값
a+=1
#주소가 바뀜
print(id(a),id(b))

m = [1,2,3]
n = m
print(id(m), id(n))
m[0]=100
#동일 래퍼런스의 value 값이 바뀜
print(m[0],n[0])
print(id(m), id(n))

#새 주소에 복사해서 만듦
k = m[:]
print(id(m),id(k))
k[0] = 200
print(k)
print(m)
print(id(m),id(k))

l = m[:]
print(l==m)     #값
print(l is m)   #래퍼런스

q= [[1,2],[3,4]]
p = q
print(p,q)
print(id(p),id(q))
print(id(p[0]),id(q[0]))
print(id(p[1]),id(q[1]))
q[0]=[0,1]
print(p,q)
print(id(p),id(q))
print(id(p[0]),id(q[0]))
print(id(p[1]),id(q[1]))

#얕은 복사(shallow copy)
q= [[1,2],[3,4]]
p = q[:]
print(p,q)
print(id(p),id(q))
print(id(p[0]),id(q[0]))
print(id(p[1]),id(q[1]))
q[0]=[0,1]
print(p,q)
print(id(p),id(q))
print(id(p[0]),id(q[0]))
print(id(p[1]),id(q[1]))

q= [[1,2],[3,4]]
p = q[:]
print(p,q)
print(id(p),id(q))
print(id(p[0]),id(q[0]))
print(id(p[1]),id(q[1]))
q[0][0] = 0
print(p,q)
print(id(p),id(q))
print(id(p[0]),id(q[0]))
print(id(p[1]),id(q[1]))

#깊은 복사(deep copy)
import copy
s = [[1,2],[3,4]]
t = copy.deepcopy(s)
