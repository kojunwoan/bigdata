'''
자료형
'''

s= 'sequence'
print(s,len(s),s.count('e'),s.find('e'),s.find('e',3),s.rfind('e'))
st='mbc'
print('mbc',type(st), id(st))

print("문자열 자르기")
print(s, s[2:4],s[:3],s[3:],s[3::2])

msg = ' hello python '
print(msg)
print(msg.strip()+"^^")
print(msg.rstrip()+msg.lstrip())

#m리스트로 만들어서 출력
msg = '구정,신정,성탄절,초파일,추석'
m = msg.split(',')
print(m)
for i in m:
    print(i)            

str_date = ['2020','07','17']
print('/'.join(str_date))