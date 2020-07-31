import random 
#예외 -> 프로그램 실행중 발생한 예상치 못한 오류 : 가벼운 오류
#예외 처리 -> 케바케

#try:
#   문장
#   문장
#except ????:
#   예외처리
#   예외처리

#사용자 정의형 예외
class EvenError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    n = int(input("숫자 입력:"))
#사용자가 입력한 값이 짝수면 실행 안함. 사용자 정의 예외어
    if n % 2 == 0:
        raise EvenError("짝수만 입력하시오")
    for i in range(10):
        a = random.randint(0,9)
        print(n/a)
except EvenError as ee:
    print(ee)
    print("짝수는 계산 안해줘")
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
except ValueError:
    print("숫자만 입력하세요")

finally:
    print("이 부분은 예외가 있던 없던 항상 실행")
#str/int 에러
#숫자/0 에러