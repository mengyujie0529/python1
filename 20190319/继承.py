import  random as r
class Fish(object):
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我的位置是：",self.x,self.y)

class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):#子类重写了父类的方法，父类的方法就被覆盖了
        self.hungry=True
        #方法1
       # Fish.__init__(self)
        #方法2
        super().__init__()

    def eat(self):
        if self.hungry:
            print("需要吃东西")
            self.hungry=False
        else:
            print("不能再吃了")

fish=Fish()
fish.move()
fish.move()

goldfish=Goldfish()
goldfish.move()
goldfish.move()

shark=Shark()
shark.eat()
shark.eat()
shark.move()
shark.move()

