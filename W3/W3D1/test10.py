m = []

m.append([100,200])
m.append([300,400,500,600,700])
m.append([900,1000,1100])
print(m)

for i in range(len(m)):
    for j in range(len(m[i])):
        print(m[i][j],end="\t")
    print()
print()
    
for i in m:
    for j in i:
        print(j,end="\t")
    print()
print()

n = [[100,50,30,20],[200,100,1],[900,1000,20,20,30,40,50],[50,70,90]]

for i in n:
    for j in i:
        print(j,end="\t")
    print()
print()