a = 1

while a != 5:
    print(a)
    a+=1

# k = 1 
# while 1:
#     k += 1
#     print(k)

for dan in range(2,10):
    for i in range(1,10):
        print(dan,"*",i,"=",dan*i)
    print("-------------------------")

for i in range(1,int(input())+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
