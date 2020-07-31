# 	ex6.py
# 	Rectangle, Triangle  의 부모 클래스인 Figure 클래스를 
# 	작성하세요 

class Figure:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def getArea(self):
        return "도형의 종류를 말해줘.."