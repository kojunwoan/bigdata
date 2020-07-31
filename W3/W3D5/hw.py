# 1.
# 	다음을 람다식으로 수정하세요 

# 	def test(x):
# 	     return x+10
lambda x : x+10





	
# 2. 
# 	"Yeah 다시 돌아왔지 내 이름 레인(RAIN) 스웩을 뽐내 WHOO! They call it! 왕의 귀환 후배들 바빠지는 중! 신발끈 꽉 매고 스케줄 All Day 내 매니저 전화기는 조용할 일이 없네 WHOO! "

# 	문자열중 공백을 기준으로 몇글짜씩인지 알아 내려고한다. 파이썬 코드로 작성하세요 
msg2 = "Yeah 다시 돌아왔지 내 이름 레인(RAIN) 스웩을 뽐내 WHOO! They call it! 왕의 귀환 후배들 바빠지는 중! 신발끈 꽉 매고 스케줄 All Day 내 매니저 전화기는 조용할 일이 없네 WHOO! ".split()
print([len(i) for i in msg2])

# 3. 
# 	2번 문자열중 글자가 4자이상인 단어만 출력하세요 
print([i for i in msg2 if len(i) >= 4])

# 4. 	도명: 도청소재지 로 만들어진 dictionary 가 있다. 
# 	do_city  = { "경기도":"수원", "강원도":"춘천"}
	
# 		dictionary 내포 표현식으로 출력 하세요 

do_city  = { "경기도":"수원", "강원도":"춘천"}
print({do:city for do,city in do_city.items()})

# 5. 
# 	지역변수와 전역변수의 차이점? 
# 전역변수는 메인함수 및 모든 함수에서 참조 가능
# 지역변수는 변수가 생성되어있는 함수 내에서만 참조 가능

# 6..
# 	다음 코드를 실행한후에 화면에 출력 되는 a의 값은 얼마인가? 
# 	a  = 100 
# 	def show():
# 	    a = 200
# 	    b = 100
# 	    print(a)  ==>200
# 	show()
# 	print(a)  ==>100


# 	왜 차이가 날까요? 	
# show 내부에서 지역변수로 a를 200으로 선언하였기 때문에 처음 값은 200이 나오고, show함수가 끝난 이후에는 전역변수 a의 값인 100이 출력된다. 


# 7. 
# 	a  = 100 
# 	def show():
# 	    ____________________
# 	    a = 200
# 	    b = 100
	    
# 	show()
# 	print(a) 

# 	200 으로 출력되게 해주려고한다. __________ 들어갈 코드는 ? global a


# 8. 
# 	지역변수의 목록을 확인하려면 어떤 명령을 사용할까? 
print(locals())

# 9.

# 	def fx():
# 	    data1  = 500    
# 	    def fx2():   
# 	        _____________________
# 	        data1 = 300  
# 	    fx2()
# 	    print(data1)
# 	fx()

# 	이 코드를 실행했을때 화면에 어떤값이 출력될까? 500


# 10.
# 	출력 결과를 300 이 나오게 하려면 __________ 에 알맞은 코드는? nonlocal data1 

# 11.
# 	일급함수의 특징 3가지를 정리하세요 
#함수를 다른 함수의 인수로 전달할 수 있다.
#함수의 반환값으로 함수를 사용 할 수 있다.
#변수나 자료구조에 저장할 수 있다.

# 12.
# 	def  tax():
# 	    a = 1.1
# 	    def mul(b):
# 	        return a*b
# 	 return mul
	
# 	getTax = tax()
# 	print(getTax(1000))

# 출력결과는 ? 1100
    
# 13.

# 	12번에서 cal 함수는 getTax 함수 호출할때 다시 꺼내서 사용되어지는데 
# 	이런 함수를 _________ 라고 한다. 
# 클로저

# 14. 
# 	일정한 규칙(패턴)을 가진 문자열을 표현하는 방법  ______________ 이라 한다. 
# 정규표현식

# 15. 
# 	사용순서 
# 		1. import re
# 		2. 컴파일에 사용 할 정규표현식 re.compile('표현식')
# 		3. 정규표현식에 맞춰볼 문자열 지정 re.compile('표현식').match('문자열')     match(첫 문자열부터 맞는 것만큼 리턴)/search(처음으로 맞는 문자열부터 맞는만큼 리턴)/findall(맞는 모든 문자열 리턴)/finditer(맞는 모든 문자열의 위치와 문자열 리턴)
		
		
# 16.
	
# 	"Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일 " 

# 	문자열중 전화번호만 찾아서 출력하고자한다. 
# 	파이썬 코드로 작성하시오.
msg16 = "Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일 " 
print([i for i in msg16.split() if i.find("-") != -1])

loc = msg16.find("010-1234-5678")
for i in range(loc,loc + len("010-1234-5678")):
    print(msg16[i], end="")
print()

# 17.
# 	16번 문제를 정규표현식으로 작성하시오 
import re
print(re.compile('\d{3}-\d{4}-\d{4}').findall(msg16))

	
		

	
	