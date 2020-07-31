#사용자로부터 글자를 입력받아 이 문자가 대문자인지 소문자인지 판단
#1. 사용자의 입력값을 받아오기
#2. 이 값의 ascii 코드값을 구한다.
#3. A : 65  a :97

data = input("한글자 입력: ")
print(data)

print(ord(data))
code = ord(data)
if code >=65 and code <=90 :
    print(data + "는 대문자입니다.",code)
elif code >=97 and code <=122 :
    print(data + "는 소문자입니다.",code)
