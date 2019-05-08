class Turtle:#乌龟类
    def __init__(self,x):
        self.num=x
class Fish:#鱼类
    def __init__(self,x):
        self.num=x
class Pool:#水池类
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)

    def print_num(self):
        print("水池里有乌龟%d只，小鱼%d条"%(self.turtle.num,self.fish.num))


pool=Pool(2,5)
pool.print_num()