# 	ex4.py 
# ----------------------------------------
# 	class Triangle 
# 	width , height
# 	getArea()
# ----------------------------------------	
# 	triangle =	Triangle (100,200) # 너비 100, 높이 200 
# 	print(triangle.getArea())  # 삼각형의 너비 구하기 
from ex6 import Figure
class Triangle(Figure):
    def __init__(self,width,height):
        super().__init__(width,height)

    def getArea(self):
        return self.width * self.height / 2
# ----------------------------------------	
triangle =	Triangle (100,200) # 너비 100, 높이 200 
print(triangle.getArea())  # 삼각형의 너비 구하기 