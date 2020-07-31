a = [3,1,8,7,2,5,4,6,9,0]
print(a)
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
