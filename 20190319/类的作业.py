#1.记录che的品牌mark,颜色color、价格price、速度speed等特征，并实现增加车辆信息、显示全部车辆信息的功能。

# class Car(object):
#
#     def __init__(self,mark,color,price,speed):
#         self.mark=mark
#         self.color=color
#         self.price=price
#         self.speed=speed
#
#     def print_car(self):
#         print('%s的颜色是%s，价格是%s,速度是%s'%(self.mark,self.color,self.price,self.speed))
#
# if __name__ == '__main__':
#     audi = Car('audi', 'red', '50w', '80km/h')
#     audi.print_car()



#2、现有一项业务 ：“Joker在BMW 4S店买了一俩BMW X7”，根据业务描述，声明相关类。
# class Person(object):
#     def __init__(self,pname):
#         self.pname=pname
# class Shop(object):
#     def __init__(self,sname):
#         self.sname=sname
# class Car(object):
#     def __init__(self,cname):
#         self.cname=cname
#
# if __name__ == '__main__':
#     person=Person("小米")
#     shop=Shop("BWM 4S")
#     car=Car("BWM X7")
#     print("%s在%s店买了一辆%s"%(person.pname,shop.sname,car.cname))

#3.创建一个由有序数值对(x, y) 组成的 Point 类，
# 它代表某个点的 X 坐标和 Y 坐标。
# X 坐标和 Y 坐标在实例化时被传递给构造器，如果没有给出它们的值，则默认为坐标的原点。
# class Point(object):
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         print("x,y分别是：",self.x,self.y)
# if __name__ == '__main__':
#     point = Point(5,6)
#     point.__str__()


#第四题
#1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person(object):
    #初始化人的信息
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        #打印人的信息
    def personInfo(self):
        print("姓名：%s，年龄：%s，性别：%s"%(self.name,self.age,self.gender))

# 2、创建Student类，继承Person类，属性有学院college，班级class，
# 重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
# 创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，
# 然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。重写__str__方法，返回student的信息。
class Student(Person):
    #初始化学生的信息

    def __init__(self,name,age,gender,collage,clas):
        super(Student,self).__init__(name,age,gender)
        self.collage=collage
        self.clas=clas
    #重写personInfo方法
    def personInfo(self):
        super().personInfo()
        print("学院：%s班级：%s"%(self.collage,self.clas))
    def study(self,teacher):
        # s=Teacher().teachObj()
        print("老师,我终于学会了！",teacher.teachObj())
# # 3、创建Teacher类，继承Person类，属性有学院college，专业professional，
# # 重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。
# # 创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序’
#
class Teacher(Person):
    #初始化老师的信息
    def __init__(self,name,age,gender,collage,professional):
        super(Teacher,self).__init__(name,age,gender)
        self.collage=collage
        self.professional=professional
    #重写personInfo方法
    def personInfo(self):
        super().personInfo()
        print("学院：%s班级：%s"%(self.collage,self.professional))
       # print("姓名：%s，年龄：%s，性别：%s,学院：%s班级：%s" % (self.name,self.age,self.gender,self.collage, self.professional))
    def teachObj(self):
        return '今天讲了如何面向对象设计程序'

if __name__ == '__main__':
    s1=Student("小明","18","boy","信息技术","计科")
    s1.personInfo()

    t1=Teacher("张三","40","man","信息技术","计科")
    s1.study(t1)
    t1.personInfo()
    print(t1.teachObj())
# 4、创建三个学生对象，分别打印其详细信息
# 5、创建一个老师对象，打印其详细信息
# 6、学生对象调用learn方法
# 7、将三个学员添加至列表中，通过循环将列表中的对象打印出来，print(Student对象)。

#5、创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。
# 在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# class User(object):
#     def __init__(self,first_name,last_name,age):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#     def describe_user(self):
#         print("姓：%s,名:%s,年龄:%s"%(self.first_name,self.last_name,self.age))
#     def greet_user(self):
#         print("hello,%s%s"%(self.first_name,self.last_name))
# if __name__ == '__main__':
#     user=User("孟","宇杰","21")
#     user.describe_user()
#     user.greet_user()

#6、可以指定一批生成的个数，可以指定数值的范围，可以调整每批生成数字的个数。
# import random
# list1=[]
# count=int(input("生成的个数为："))
# numberRangeSmall=int(input("生成数的最小值是："))
# numberRangeLarge=int(input("生成数的最大值是："))
# i=1
# while i <= count:
#     list1.append(random.randint(numberRangeSmall,numberRangeLarge))
#     i+=1
# print(list1)

#7.有如下值集合[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
list1=[11,22,33,44,55,66,77,88,99,90]
list2=[]
list3=[]
dict1={}
for i in range(len(list1)):
    value = list1[i]
    v = dict1.fromkeys(['k1','k2'],[])
    if value>=66:
        list2.append(value)
    else :
        list3.append(value)
    v['k1']=(list2)
    v['k2']=(list3)
print(v)

#8.使用while，再完成以下图形的输出
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
# i=1
# j=1
# while i<=5:
#     while j<=5-i or j>=5+i:
#         print("")
#         j+=1
#     while j>5-i or j<5+i:
#         print("*")
#     print("\n")
#     i+=1

#9.　nums=[2,7,11,15,1,8,7]
#请找到列表中任意两个元素相加能够等于9的元素集合，列[(2,7), (1,8)]
# nums=[2,7,11,15,1,8,7]
# list1=[]
# def add(num):
#     for i in range(0,len(num)):
#         for j in range(i+1,len(num)):
#             if num[i]+num[j] == 9:
#                 list1.append((num[i],num[j]))
# add(nums)
# print(list1)



'''
6公里(含)内3元;6公里至12公里(含)4元;12公里至22公里(含)5元;22公里至32公里(含)6元;32公里以上部分，每增加1元可乘坐20公里。
使用市政交通一卡通刷卡乘坐轨道交通，每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;
满150元以后的乘次，价格给予5折优惠;支出累计达到400元以后的乘次，不再享受打折优惠。
要求：
假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁；
每月月初小明第一次刷公交卡时，扣款5元；
编写程序，从键盘获取距离，帮小明计算，如果不使用市政交通一卡通的每月总费用，和使用市政交通一卡通的每月总费用

'''

# def NoCarPay(pathLength):
#
#     if pathLength<=6:




