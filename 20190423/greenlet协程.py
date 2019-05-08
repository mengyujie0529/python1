from greenlet import greenlet
import  time
def w1():
    for i in range(5):
        print("w1",i)
        g2.switch()


def w2():
    for i in range(5):
        print("w2",i)
        g1.switch()
g1=greenlet(w1)
g2=greenlet(w2)




