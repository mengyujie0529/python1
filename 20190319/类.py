# class Ball(object):
#     def setName(self,name):
#         self.name=name
#     def kick(self):
#         print("我叫%s"%self.name)
#
# a=Ball()
# a.setName("A")
# b=Ball()
# b.setName("B")
#
# a.kick()
# b.kick()

class Ball(object):
    def __init__(self,name):
        self.name=name
        num=1
    def kick(self):
        print("我叫%s"%self.name)

b=Ball("B")
b.kick()