#class 클래스명:
#   속성
#   함수, method()
#   객체 : 사물
#   class : 설계도
#   대상 : instance(메모리를 가지고 있음.)

class Human:
    # __ 메서드를 매직메서드
    def __init__(self):
        print("초기화 함수")
    
    def eating(self):
        print("냠냠 맛있게 먹어요")

    def sleeping(self):
        print("쿨쿨.......... Zzz")

hong = Human()  #instance   hong = new Human() -> 파이썬 없음
print(hong)
hong.eating()
hong.sleeping()

lim = Human()
lim.eating()
lim.sleeping()