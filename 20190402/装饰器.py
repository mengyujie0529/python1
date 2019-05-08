'''实现装饰器'''

def wrap1(func):
   # print('begin wrap1')
    def inner():
        print('begin wrap1 inner')
        func()
   # print('end wrap1')
    return inner


def wrap2(func):
   # print('begin wrap2')
    def inner():
        print('begin wrap2 inner')
        func()
   # print('end wrap2')
    return inner


#@wrap1
@wrap2
def cost():
    print('付款')


#cost = wrap2(cost)
#cost = wrap1(wrap2(cost))
print('#######################################################')

def wrap1(func):
   # print('begin wrap1')
    def inner():
        print('begin wrap1 inner')
        func()
   # print('end wrap1')
    return inner


def wrap2(func):
   # print('begin wrap2')
    def inner():
        print('begin wrap2 inner')
        func()
   # print('end wrap2')
    return inner


#@wrap1
@wrap2
def cost():
    print('付款')


#cost = wrap2(cost)
#cost = wrap1(wrap2(cost))
print('#######################################################')

if __name__ == '__main__':
    cost()