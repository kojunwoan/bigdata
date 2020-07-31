# 정규표현식(regular expression) L 일정한 규칙(패턴)을 가진 문자열을 표현하는 방법#정규표현식
# 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어
# 대부분의 텍스트 펹비기와 프로그램언어에서 문자열의 검색과 치환을 위해 지원하고 있다.
# https://regexr.com


import re

#re.match('패턴','문자열')

print(re.match('Hello','Hello python world'))
# 문자열 : .find

print('Hello python world'.find('Hello'))

#첫글자 ^H
print(re.match('^H','Hello python world'))
print(re.search('^H','Hello python world'))
#끝글자 $d
print(re.match('world$','Hello python world'))
print(re.search('world$','Hello python world'))

#010-1234-5678
print(re.match('\d+','010-1234-5678'))
print(re.match('\d*','010-1234-5678'))

#aaabbb


if re.match('a+b','aaabbb'):
    print(re.match('a+b','aaabbb'))
else:
    print("ㅠㅠㅠ")

print(re.match("[가-힣]+","불금흰달려보자!"))
# for i in range(ord("가"),ord("힣")):
#     print(chr(i),end='')

#ab9cd(o),ab9999cd(x)
print(re.match('[a-z]+9[a-z]+','ab9cd'))
print(re.match('[a-z]+9[a-z]+','ab9999cd'))