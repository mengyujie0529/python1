def wapper(func):
    def inner(total):
        print("***")
        func(total)
    return  inner

@wapper
def cost(total):
    print(total)

if __name__ == '__main__':
    cost(10)