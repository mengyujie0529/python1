class MyException(Exception):
    #自定义异常
    def __init__(self):
        super().__init__()
        self.errormsg="自定义报错信息"
    def __str__(self):
        return self.errormsg

try:
    s=input('请输入一个值')
    if len(s) < 3:
        raise MyException
except MyException as e:
    print("进入except")
    print(e)
# else:
#     print("进入else")
# finally:
#     print("都要进入")