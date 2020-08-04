#모듈 : 연관된 함수의 모음
#__name__ <- 모듈의 이름을 가진 변수
author = "고준완"
print(__name__) # __m^.^m__
def raise_sal(sal):
    '''
    급여를 전달하면 10%인상된 급여를 리턴
    Entering a salary returns a 10% increase in salary
    '''
    return sal*1.1

def reduse_sal(sal):
    return sal*0.8

    
if __name__ == "__main__":
    print(raise_sal(3000))
    print("잘 나오나??",author)