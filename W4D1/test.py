# 1. 두 개의 정수 값을 받아 두 값의 평균을 구하는 함수를 작성하고 임의의 값으로 실행 하세요 
def avg(a, b):                                      #매개변수 a,b를 받는 avg 함수 정의
    return (a+b)/2                                  #반환값은 (a+b)/2 => 평균
if __name__ == "__main__":                          #모듈명이 현재 모듈 __main__일때
    print(avg(200,100))                             #200과 100을 매개변수로  avg 함수 호출




# 2. sList 는 학생들의 영어 점수로 만든 리스트 이다.  최댓값과 최솟값을 반환하는 함수를 작성하세요.
sList = [ 90, 80, 23, 55, 32, 50, 95, 90, 85, 60, 75, 35, 88, 92]
def max_min(listData):                              #매개변수를 리스트로 받는 max_min 함수 정의
    return max(listData),min(listData)              #리스트중에서 max값과 min 값을 반환
if __name__ == "__main__":                          
    print(max_min(sList))                           


# 3. e:/dev/python_workspace/  경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환하는 함수를 작성하세요.
def get_list(path):                                 #경로를 매개변수로 받는 get_list 함수 정의
    from os import listdir                          #os모듈의 listdir함수 임포트
    return [file for file in listdir(path) if file.endswith('txt')]     #매개변수로 받은 경로의 파일중 txt로 끝나는 파일을 리스트로 만들어서 반환
if __name__ == "__main__":
    print(get_list("e:/dev/python_workspace/"))

# 4. 오늘의 월 일을 출력하는 함수를 작성하세요 
from time import gmtime
def get_todate():
    return "{}월 {}일".format(gmtime().tm_mon,gmtime().tm_mday)     #month와 날짜를 가져와서 반환
if __name__ == "__main__":
    print(get_todate())   # 7월 27일 



# 5.  다음 함수를 작성하세요 
def get_triangle_area(width, height):
    return width * height / 2                                       #가로 x 높이 / 2 
if __name__ == "__main__":
    print(get_triangle_area(100,200))  # 10000

# 6.
def get_circle_area(radius):
    from math import pi 
    return pi * radius**2                                     #pi*r^2
if __name__ == "__main__":
    print(get_circle_area(10))  # 314.1592653589793



# 7. nList 에 랜덤하게 1부터 100사이 의 정수 20개 를 넣는다. 
from random import randint
nList = [randint(1,100) for i in range(20)]                     #리스트 내포 사용으로 20개 값 넣기.
if __name__ == "__main__":
    print(nList)

# 8. nList에 홀수 가 몇개가 있는지 를 리턴하는 함수를 구하세요 
def get_odd(listdata):
    cnt = 0                                                     #홀수 갯수를 저장할 변수 cnt
    for i in listdata:                                          #listdata에서 값을 순서대로 가져와서
        if i%2 == 1:                                            #홀수이면
            cnt += 1                                            #cnt를 1 증가시킨다.
    return cnt                                                  #모든 값을 비교하고 cnt를 반환 한다.
if __name__ == "__main__":
    print(get_odd(nList))  # n


# 9.  5자로 구성된 랜덤문자를 만들어 20개를 넣는다. 
wordList = []   # wordList = ['abcde', 'xwdsd, ....]
for i in range(20):
    msg = ""                                                    #5자 짜리 문자를 담을 변수(1개 만들때마다 초기화)
    for j in range(5):                                          #5번 반복한다
        msg += chr(randint(97,122))                             #msg변수에 소문자(아스키코드 97~122)중 한개의 문자 추가하여
    wordList.append(msg)                                        #만들어진 5자 문자를 배열에 담는다.
if __name__ == "__main__":
    print(wordList)

# 10. wordList 요소에서 뒤에 3글자만 자른 문자를 갖는 리스트를 출력하는 함수를 작성하세요
def get_last_word(listdata):
    return [i[-3:] for i in listdata]                           #listdata에서 값들을 꺼내고 뒤에 3자리만 슬라이스 하여 새로운 배열에 담는다. 그리고 그것을 반환한다.
if __name__ == "__main__":
    print(get_last_word(wordList))  #  [ cde ,  dsd  , .... ]

# 11. 지금까지 만들어진 함수를 test 라는 모듈로 작성하세요
#완료

# 12. 현재 파일에서 실행할때만 테스트 결과가 출력되게 작성하세요
#완료

# 13. ex1.py 파일을 작성하고  test. get_circle_area(300)을 실행시켜보세요
#완료

# 14. 다른 모듈의 함수를 불러 사용하는 방법 3가지를 정리하세요 
# import 모듈명
# from 모듈명 import 함수명
# from 모듈명 import *



# 15. 비의 깡 가사를 rain.txt 파일에 저장하세요 
ggang = '''
Yeah 다시 돌아왔지
내 이름 레인(RAIN)
스웩을 뽐내 WHOO!
They call it! 왕의 귀환
후배들 바빠지는 중!
신발끈 꽉 매고
스케줄 All Day
내 매니저 전화기는
조용할 일이 없네 WHOO!

15년을 뛰어
모두가 인정해 내 몸의 가치
허나, 자만하지 않지
매 순간 열심히 첫 무대와 같이
타고난 이 멋이 어디가
30 sexy 오빠
또 한번 무대를 적셔
레인이펙트
나비 효과

화려한 조명이 나를 감싸네
시간이 멈추길 기도해
but, I’m not gonna cry yeah
불 꺼진 무대 위 홀로 남아서
떠나간 그대의 목소릴 떠올리네
나 쓰러질 때까지 널 위해 춤을 춰

허세와는 거리가 멀어
난 꽤 많은 걸 가졌지
수많은 영화제 관계자
날 못 잡아 안달이 나셨지
귀찮아 죽겠네 알다시피
이 몸이 꽤 많이 바빠
섭외 받아 전세계 왔다 갔다
팬들이 하늘을 날아 WHOO!

TV 드라마, 영화 yeah!
I get it all
이젠 모두를 붙잡을 노래를 불러
볼륨은 올리고
재 등장과 동시
완전 물 만나 call me 나쁜 오빠
무대를 다시 한번 적시지
레인이펙트
나비 효과

화려한 조명이 나를 감싸네
시간이 멈추길 기도해
but, I’m not gonna cry yeah
불 꺼진 무대 위 홀로 남아서
떠나간 그대의 목소릴 떠올리네
나 쓰러질 때까지 널 위해 춤을 줘
'''                                                                         # 노래 가사를 변수로 지정하여
with open("./W4D1/rain.txt", 'w', encoding='utf-8') as file0:               
    file0.write(ggang)                                                      # 파일에 쓴다.

# 16.
# 	rain.txt 에서 4글자 단어는 모두 몇개인가? 
with open("./W4D1/rain.txt",'r', encoding='utf-8') as file1:                #파일을 읽기전용으로 불러와서
    print(len([word for word in file1.read().split() if len(word) == 4]))   #파일을 띄어쓰기 단위로 끊어서 단어를 만든후, 이 단어의 길이가 4일경우 배열에 담는다. 나중에 이 배열의 크기를 출력하면 길이가 4인 단어의 갯수가 출력

# 17.
# 	사용자가 입력한 디렉토리의 파일과 디릭토리 목록을 dir.txt 파일에 저장하세요
import os 
with open("./W4D1/dir.txt", 'w', encoding='utf-8') as file2:
    for name in os.listdir(input("디렉토리를 입력하시오 : ")):                  #사용자에게 디렉토리명을 입력받아서, 해당디렉토리의 디렉토리들과 파일의 이름을
        file2.write(name+"\n")                                                #파일에 쓴다.

# 18.
# 	로또 번호를 생성해서  lotto.txt 파일에 한줄씩 저장하세요 
# ex)
# 	3
# 	15
# 	29
# 	32
# 	35
# 	41
from random import randint
with open('./W4D1/lotto.txt', 'w', encoding='utf-8') as file3:
    l = set()                                                           #set을 만들어서
    while len(l)<6:                                                     #set의 길이가 6이 될때까지
        l.add(randint(1,45))                                            #숫자를 담으면 중복이 없는 6개의 숫자를 받을 수 있다.
    for n in l:                                                         #받은 숫자를
        file3.write(str(n)+"\n")                                        #파일에 쓴다.


# 19.
# 	랜덤하게 소문자 3자를 생성해서  randomchar.txt 파일에 저장하세요 
with open('./W4D1/radomchar.txt', 'w', encoding='utf-8') as file4:
    for i in range(3):                                                  #3번 반복
        file4.write(chr(randint(97,122)))                               #랜덤 소문자를 만들어서 파일에 쓴다.

# 20.  다음 내용을 stock.csv 로 저장하세요 
Stock = [['종목번호','회사명','현재주가'],['035720','카카오',326500],['005930','삼성전자',55600],['047820','초록뱀',1590]] 
with open('./W4D1/stock.csv', 'w') as file5:
    for i in Stock:
        for j in i:
            file5.write(str(j)+',')
        file5.write("\n")