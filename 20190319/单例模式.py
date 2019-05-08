'''实现单例模式'''
class Person(object):
    '''这是一个单例类'''
    __instance = None
    #这个类属性存储的是实例对象
    def __new__(cls,*args,**kwargs):
        if not cls.__instance:
            #如果__instance没有存储实例对象
            cls.__instance=super(Person,cls).__new__(cls,*args,**kwargs)
        return cls.__instance
if __name__ == '__main__':

    ming = Person()
    print(id(ming))

    ming2 = Person()
    print(id(ming2))