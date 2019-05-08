import gevent
from gevent import  monkey
import time
#必须 先写下面这句话，用于给所有的耗时操作打补丁，用于协程之间的自动切换
monkey.patch_all()

def w1():
    for i in range(5):
        print("w1",i)
        time.sleep(0.1)
        

def w2():
    for i in range(5):
        print("w2",i)
        time.sleep(0.1)
g1=gevent.spawn(w1)
g2=gevent.spawn(w2)
g1.join()
g2.join()
exit()
