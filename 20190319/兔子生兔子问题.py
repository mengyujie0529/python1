def rabbit(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return rabbit(n-1)+rabbit(n-2)

n=int(input('月数：'))
result=rabbit(n)
print(result)