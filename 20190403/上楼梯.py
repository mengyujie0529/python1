'''
n     1 2 3 4 5 6
方法  1 2 3 5 8 13
'''

def cal(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return cal(n-1)+cal(n-2)

if __name__ == '__main__':
    num=int(input("n的值："))
    print("有",cal(num),"种方法")