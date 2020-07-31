class GuGuDan:
    def __init__(self):
        self.dan = 0
    
    def print(self):
        for i in range(1,10):
            print("{} * {} = {}".format(self.dan,i,self.dan*i))

g = GuGuDan()

g.dan = 3
g.print()