#import 하는 3가지 방법
#1. import 모듈명
#2. from 모듈명 import 함수명   (이 경우 다른 모듈에 동일한 이름의 함수가 있을 경우 충돌날 우려가 있음)
#3. from 모듈명 import *        (모듈.함수() 안하고 함수()로 사용)
import math
from random import randint
from random import *
print(randint(0,1))
print(dir())