# 1.   object , class , instance 란? 
'''
class : 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면
object : 클래스로 만든 피조물   a 는 객체
instance : 클래스로 만든 객체   a 는 A클래스의 인스턴스
'''
# 2.    
class Man:
    def __init__(self):
        self.name = "홍길동"
        self.eye = 2
        self.gender = "남"
        self.arm = 2
        self.age = 20
        self.job = "도적"
        self.character = "스틸"

    def steal(self):
        print("내꼬내꼬 다 내꼬얌!!!")

    def run(self):
        print("헛둘 헛둘")

    def runrun(self):
        print("땀나게 달려요")
    
    def magic_move(self):
        print("동해 번쩍 서해 번쩍")
m = Man()

print(m.name) # 홍길동
print(m.eye) # 2 
print(m.gender)# 남
print(m.arm) # 2
print(m.age) # 20
print(m.job) # 도적
print(m.character)# 스틸 

m.steal() # 내꼬내꼬 다 내꼬얌!!! 
m.run() # "헛둘 헛둘"
m.runrun() # 땀나게 달려요
m.magic_move() # 동해 번쩍 서해 번쩍


# 3.	변수명명법?

# 4. 
# 	ex4.py 
# ----------------------------------------
# 	class Triangle 
# 	width , height
# 	getArea()
# ----------------------------------------	
# 	triangle =	Triangle (100,200) # 너비 100, 높이 200 
# 	print(triangle.getArea())  # 삼각형의 너비 구하기 

# 5. 
# 	ex5.py
# ----------------------------------------
# 	class Rectangle
# 	width , height
# 	getArea()
# ----------------------------------------
# 	r = Rectangle(200,300)
# 	print(r.getArea())  # 사각형의 너비 구하기 

# 6.
# 	ex6.py
# 	Rectangle, Triangle  의 부모 클래스인 Figure 클래스를 
# 	작성하세요 
	
# 7. 
# 	Rectangle, Triangle 은 Figure 클래스의 구현클래스로 코드를 변경합니다.

# 8. 
# 	Rectangle, Triangle 의 getArea() 는 Figure 클래스 의 getArea() 를 
# 	method overriding 시켜줍니다. 

# 9.
# 	두점 사이의 거리를 계산하는 pytagoras()를 완성하세요 
from math import sqrt
class util:
    @staticmethod
    def pytagoras(x1,y1,x2,y2):
        return sqrt((x1-x2)**2+(y1-y2)**2)
print(util.pytagoras(100,100, 200 ,200))
	
# 	참고 : math.sqrt(4) ==> 2 

# 10.
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def get_xy(self):
        print((lambda : (self.x, self.y))(),end="")
    def move(self,x,y):
        self.get_xy()
        print(" ==> ",end="")
        self.set_x(x)
        self.set_y(y)
        self.get_xy()

p = Point(100,100) # (x, y) 좌표 
p.set_x(200)  # x좌표값을 200으로 변경
p.set_y(300)  # y좌표값을 300으로 변경
p.get_xy() # (200,300) 형태로 출력 
print()
p.move(500,300) # (200,300) ==> (500,300)
# 	                     # 메세지를 출력하고 x <= 500 y <=300을 담는다.
	
# 	참고 ) 모든 메세드는 인스턴스 메서드 모든 속성는 인스턴스 속성


	