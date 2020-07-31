msg = input("단어를 입력하시오.")
for i in range(len(msg)):
    if ord(msg[i]) >=65 and ord(msg[i]) <=90 :      #대문자일때
        print(chr(ord(msg[i])+32),end="")           #소문자로 바꾸고
    elif ord(msg[i]) >=97 and ord(msg[i]) <=122 :   #소문자일때
        print(chr(ord(msg[i])-32),end="")           #대문자로 바꿔라
    else:
        print(msg[i],end="")
