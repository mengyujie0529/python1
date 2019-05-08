
class P20(object):
    def __init__(self):
        self.price = 6000
    def buy(self):
        print("P20")

class P30(object):
    def __init__(self):
        self.price = 8000
    def buy(self):
        print("P30")

def creat(type):
    if type == 'P20':
        phoneP20 = P20()
        return phoneP20
    if type == 'P30':
        phoneP30 = P30()
        return phoneP30

class HuaWeiShop(object):
    def sale(self):
        phone = creat('P20')
        return phone

p1 = HuaWeiShop.sale('P20')
p1.buy()