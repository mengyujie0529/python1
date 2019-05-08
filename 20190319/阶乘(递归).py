#不用递归写阶乘
def jiecheng(num):
    result=num
    for i in range(1,num):
        result=result*i
    return  result

n=int(input('输入一个数'))
res=jiecheng(n)
print(res)
#用递归写阶乘
def digui(n):
    if n==1:
        return 1
    else:
        return n*digui(n-1)
number=int(input('输入一个数'))
res2=digui(number)
print(res2)