import  time
def w1():
    for i in range(5):
        print(i)
        yield
        time.sleep(0.1)
def w2():
    for i in range(5):
        print(i)
        yield
        time.sleep(0.1)
w1=w1()
w2=w2()
while True:
    next(w1)
    next(w2)