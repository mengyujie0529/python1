#1.给定一个list a, 满足a[i+1] >= a[i], 给定int key ,找出list a 中第一个大于等于key的元素的index，无满足要求的元素则返回-1。
# a=[1,2,3,4,5,6,7,8,9]
# def find(key):
#     for index in range(len(a)):
#         if a[index] >= key:
#             return index
#     return -1
# ret=find(5)
# print(ret)


#2.求结果v = dict.fromkeys(['k1','k2'],[])v[‘k1’].append(666)print(v)v[‘k1’] = 777print(v)
# v = dict.fromkeys(['k1','k2'],[])
# v['k1'].append(666)
# print(v)
# v['k1'] = 777
# print(v)

#3.按照一下要求定义一个游乐园门票类，并尝试计算2个成人+1个小孩子平日票价
# 1.平日票价100元
# 2.周末票价为平日票价120%
# 3.儿童半价

# def pay(m,n,weekend):#买票,m表示成人个数，n表示小孩个数,weekend参数1表示周末，0表示不是周末
#     if weekend==1:#周末价格是120
#         price=120
#     else:
#         price=100#平时价格是100
#     allPay=price*m+price*n*0.5#计算总价格=成人个数*价格+儿童个数*原来的价格*0.5
#     print(allPay)
# ret=pay(2,1,0)










#4.从开发的代码库中得到一组数据，表示每个文件的代码变更情况
#  {'login.py': 'a 8 d 2 u 3', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5'}
# 其中 a表示新增行数，d表示删除行数，u表示修改行数。login.py的变更行数为13
dict1={'login.py': 'a 8 d 2 u 3', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5'}
# def change(dic):
#     for i in len(dic):
#         res=[]
#         for index in


#5.定义一个函数func(listinfo) listinfo:为列表，listinfo = [133, 88, 24, 33, 232, 44, 11, 44]，返回列表小于100，且为偶数的数
# def func(listinfo):
#     for index in range(len(listinfo)):
#         if listinfo[index] < 100 and listinfo[index]%2 == 0:
#             print(listinfo[index])

# list1 = [133, 88, 24, 33, 232, 44, 11, 44]
# # ret = func(list1)
# # print(ret)
# ret=[i for i in list1 if i < 100 and i%2 == 0]#列表表达式
# print(ret)


#6.自己定义一个异常类，继承Exception类, 捕获下面的过程：判断raw_input( )输入的字符串长度是否小于5， 如果小于5，
# 比如输入长度为3则出:" The input is of length 3,expecting at least 5'，大于5输出"print success' 
# class MyException(Exception):
#     # 自定义异常
#     def __str__(self):#如果打印错误信息，必须写在这个方法
#         self.errormsg="这是错误"
#         return self.errormsg
# try:
#     raw = input("请输入一个字符串:")
#     # print(len(raw))
#     if len(raw) < 5:
#         raise MyException
#
# except MyException as e:
#     print("The input is of length %s,expecting at least 5"%len(raw))




#7.完美立方：找到大于1的4个整数满足完美立方等式：a3=b3+c3+d3（例如123=63+83+103）。
# 编写一个程序，对于任意给定的正整数N（N ≤100），寻找所有的四元组（a,b,c,d），满足a3=b3+c3+d3，其中1<a，b，c，d≤N。





#8.恺撒密码：凯撒密码是古罗马凯撒大帝用来对军事情报进行加解密的算法，
# 它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，
# 即，字母表的对应关系如下：A-D,B-E,C-F
# list1=['A','B','C','D','E','F']
# def CaesarCipher():
#     for index in range(len(list1)):
#         list1[index]=ord(list1[index])+3 #先把list1的元素从字符串转化为ASCII值，在➕上3
#         list1[index]=chr(list1[index])#在把加完3的ASCII值转化为字符串
#     print(list1)
# ret=CaesarCipher()





#3位水仙花数计算：“3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身。
# 例如：ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC。
def narcissistic():
    #三位水仙花数计算
    for num in range(100,999):
        a = int(num / 100)  # 百位
        b = int((num / 10) % 10)  # 十位
        c = int(num % 10)  # 个位
        #如果A的3次方＋B的3次方＋C的3次方 = ABC
        if a*a*a+b*b*b+c*c*c == num:
            print(num)
            print(",\t")
ret=narcissistic()
print(ret)

#给定两个非负整数x和y，如果A等于x^i+y^j，其中整数i>= 0且j>=0，那么我们认为A是一个"精致"的数。
# 返回小于或等于n(n<=200)的所有A组成的列表。结果列表中每个值最多出现一次，同时请使用sorted保证结果唯一。
# 输入格式：共三行，每一行为一个整数，分别是x y n
# 输出格式：共一行，为一个列表。
# 输入样例：
# 1
# 2
# 5
# 输出样例：[2, 3, 5]
def Number():
    list1=[]#储存结果
    x = int(input("输入x:"))
    y = int(input("输入y:"))
    n = int(input("输入不超过200的数n:"))
    for i in range(0,n):#n的范围过大，所以导致结果过输出的数目会多几个
        for j in range(0, n):
            number=x**i+y**j
            list1.append(number)
            list1.sort()#排序
            set1=set(list1)#去重
            list2=list(set1)
    print(list2)
ret=Number()







