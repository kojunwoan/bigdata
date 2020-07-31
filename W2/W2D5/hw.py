# 1.
# 	1부터 100까지 출력 

# 1
# 2
# 3
# 4
# ..
# 99
# 100

for i in range(1,101):
    print(i)



# 2.

# 11111
# 22222
# 33333
# 44444
# 55555
for i in range(1,6):
    print(str(i)*5)

# 3

# 99999
# 88888
# 77777
# 66666
# 55555
for i in range(9,4,-1):
    print(str(i)*5)



# 4.  이중for문 사용 
# 1234
# 5678
for i in range(2):
    for j in range(1,5):
        print(i*4+j,end="")
    print()

num=1
for i in range(2):
    for j in range(4):
        print(num,end="")
        num+=1
    print()


# 5. 

# 구구단8단 출력 
for i in range(1,10):
    print("8 *",i,"=",8*i)
# 6.

# 2단부터 9단까지 출력 
for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)



# 7.  구구단 3단 출력 

# 3   * 1 =  3   3 * 2 = 6   3 * 3 = 9 ...    3  * 9  = 27
for i in range(1,10):
    print("3 *",i,"=",3*i,end="\t")

# 8. 

# 1
# 11
# 111
# 1111
# 11111
for i in range(1,6):
    print("1"*i)


# 9 
# 	1
# 	2
# 	...
# 	...
# 	100
for i in range(1,101):
    print(i)

# 10  1부터 100 합계를 출력
# 	5050
sum = 0
for i in range(1,101):
    sum += i
print(sum)


# 11
# 	*
# 	**
# 	***
# 	****
# 	*****
for i in range(1,6):
    print("*"*i)

# 12
# 	1
# 	12
# 	123
# 	1234
# 	12345
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()




# 13. 

# 	2 * 1 = 2   2 * 2 = 4 ... 2 * 9 = 18
# 	3 * 1 = 3   3 * 2 = 6 ... 3 * 9 = 27
# 	...			   ...
# 	9 * 1 = 9   9 * 2 = 18 ... 9 * 9 = 81
for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end="\t")
    print()


# 14. 

# 	*****
# 	****
# 	***
# 	**
# 	*	
for i in range(5,0,-1):
    print("*"*i)


# 15.
# 	time Converter 

# 	시간입력:90061

# # 	1일 1시간 1분 1초 입니다.	


time = [60,60,24]                       #초, 분, 시간
msg1 = [int(input("시간입력:"))]        #몇시간인지 입력받고, 이를 리스트의 0번에 넣음
msg2 = ["일","시","분","초"]            #나중에 출력할때 쓰려고 만듬
for i in time:                          #각 시간의 단위로 나눌겁니다.
    msg1[0], a = divmod(msg1[0],i)      #입력받은 시간을 초>분>시간으로 나누고 몫은 다음 단위시간이므로 리스트0번에 다시 넣어버리고
    msg1.insert(1,a)                    #나머지는 그단위의 시간이기 때문에 1번으로 넣는다.
while not(msg1[0]):                     #만약 입력된 시간이 작아서 
    del msg1[0]                         #일자가 안나올경우 지워버린다.
    del msg2[0]                         
for i in range(len(msg1)):              #시간 길이만큼 
    print(msg1[i],msg2[i],end="\t")     #출력한다.

# t = int(input("시간입력:"))
# print(t//60//60//24,"일",t//60//60%24,"시",t//60%60,"분",t%60,"초")

# 16.

# 	잔돈교환기(큰 단위 화폐순으로 ) 

# 	입력 : 67921 

# 	50000권 : 1매
# 	10000권 : 1매
# 	5000권  : 1매
# 	1000권  : 2매
# 	500권   : 1개
# 	100권   : 4개
# 	50권    : 0개
# 	10권    : 2개
# 	1원     : 1개 


unit = [50000,10000,5000,1000,500,100,50,10,1]  #환전시 참고할 돈의 단위이다.
m = int(input("입력 : "))                       #돈을 m에 입력 받고
for u in unit:                                  #환전 금액이 높은 순으로 반복문을 실행한다.
    a, m = divmod(m,u)                          #입력받은 금액을 환전단위로 나누어서 몫은 해당 a라고 하고, 나머지는 다음 단위 환전을 위해 다시 m에 넣는다.
    print(str(u)+"원\t:",a,"개")                #직전에 저장한 a는 해당 단위의 갯수이기 때문에 출력.