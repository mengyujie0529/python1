def hanoi(n,x,y,z):#n代表多少个盘子，xyz表示3根柱子
    if n==1:
        print(x,'-->',z)
    else :
        #将前n-1个盘子从x移动到y上
        hanoi(n-1,x,z,y)
        #将最底下的最后一个盘子从x移动到z上
        print(x,'-->',z)
        #将y上的n-1个盘子移动到z上
        hanoi(n-1,y,x,z)

n=int(input('请输入汉诺塔的层数'))
result=hanoi(n,'x','y','z')
print(result)