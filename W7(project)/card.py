class Card:
    def __init__(self,ctype,rank,name,img):
        self.type = ctype
        self.rank = rank
        self.name = name
        self.frontImg = "E:/dev/python_workspace/W7(project)/img/{}.jpg".format(self.type)
        self.backImg = "E:/dev/python_workspace/W7(project)/img/0.jpg"
    