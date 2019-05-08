def wapper(func):
    def inner(type):
        if type == 1:
            print("你是管理员")
        elif type == 2:
            print("你是普通用户")
        func()
    return inner

@wapper
def judge():
    print("*****")

if __name__ == '__main__':
    judge(1)
    judge(2)