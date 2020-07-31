#tuple : 읽기전용 리스트

t = 'a','b','c','d'
print(t, type(t))

t2 = ('a','b','c','d')
print(t2, type(t2))
print(t2, len(t))
print(t.count('a'))
print(t.index('b'))

x=(1,2,3)
# x[0] = 10 읽기전용이라서 안됨 
print(x)

x2 = (3)
x3 = (3,)
print(x2,type(x2))
print(x3,type(x3))

print(x)
y = list(x)
y[2] = 30
print(y)
x=tuple(y)
print(x)

t1=(10,20)
y1=list(t1)
y1[0], y1[1] = y1[1], y1[0]
t1=tuple(y1)
print(t1)

a, b = t1
a, b = b, a
t1 = (a,b)
print(t1)