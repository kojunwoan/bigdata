import re
p = re.compile('[a-z]+')
print(p,type(p))
# '패턴 : 정규식을 컴파일한 결과'

# '문자열 검색'
# 'match() : 문자열의 처음부터 정규식과 100% 매치되는지 조사'
# 'search() : 문자열 전체를 검색하여 하나의 구간이라도 정규식과 매치되는지 조사'
# 'findall() : 정규식과 매치되는 모든 문자열을 리스트로 리턴함'
# finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴함

m = p.match('regular expression')
m = p.match('9regular expression')
print(m)
if m:
    print(m.group())        #값을 꺼낼때 .group() 사용
else:
    print("no match")

result = p.search("999999999 aaaaaaaabbbbbb")
print(result)

result2 = p.findall("hello python world  today is monday")
print(result2)

for i in result2:
    print(i)

result3 = p.finditer("today is monday")
print(result3)
for data in result3:
    print(data)
    print(data.start(), ":", data.end())
    print(data.group())

msg = " 999,999   smartphone  bbb@naver.com  aaa@gmail.com"
p1 = re.compile('\w+@\w+.\w+')
#이메일만 선택해서 출력
for email in p1.findall(msg):
    print(email)