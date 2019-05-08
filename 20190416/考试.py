# 1.说说你对Python拷贝的了解以及需要注意的地方，并用代码实现list a的拷贝, a=[1,2,3]
# import copy
# list1=[1,2,3]
# list2=list1.copy()
# list3=copy.deepcopy(list1)
# print(list1,list2,list3)
# 拷贝分为浅拷贝和深拷贝，浅拷贝地址不一样，拷贝之后两个列表没有关系，深拷贝后两个地址相同，修改其中一个，两个一起变化。


#2.在下面函数中，写出print对应的值，分析为什么会出现这个结果？对该代码的修改有什么建议？
# def fn(a=[]):
#     a.append(1)
#     return a
# b = fn([1, 2, 3])
# print(b)
# c = fn()
# print (c)
# d = fn()
# print (c)
# print (d)


# dict1={'a':1,'b':2}
# print(dict1.items())
# print(dict1.iter())
# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时，共有5个数相加)，几个数相加有键盘控制。
# def add(num):
#     n = int(input("输入有几个数相加："))
#     ret = 0
#     for i in range(n):
#         for j in range(i+1):
#             ret += num * 10**j
#     print(ret)
# if __name__ == '__main__':
#     add(5)
###嵌套循环输出10-50中个位带有1-5的所有数字
# for i in range(10,50):
#
#     if i % 10 == 1 or i % 10 == 2 or i % 10 == 3 or i % 10 == 4 or i % 10 == 5:
#         print(i)

#企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# 求应发放奖金总数def Bonus(i):
#     if i <= 10:
#         bonus = i*0.01
#     elif i>10 and i<=20 :
#         bonus = 10*0.01 + (i-10)*0.075
#     elif i>20 and i<=40 :
#         bonus = 10*0.01 + (20-10)*0.075 + (i-20)* 0.05
#     elif i>40 and i<=60 :
#         bonus = 10*0.01 + (20-10)*0.075 + (40-20)* 0.05 + (i-40)*0.03
#     elif i > 60 and i <= 100:
#         bonus = 10 * 0.01 + (20 - 10) * 0.075 + (40 - 20) * 0.05 + (60 - 40) * 0.03 + (i - 60) *0.015
#     elif i>100:
#         bonus = 10 * 0.01 + (20 - 10) * 0.075 + (40 - 20) * 0.05 + (60 - 40) * 0.03 + (100 - 60) * 0.015 + (i-100)*0.01
#     return bonus
# if __name__ == '__main__':
#     i = int(input("输入利润I："))
#     ret = Bonus(i)
#     print("应发奖金：",ret,"万元")

# 使用Process创建1个子进程，让子进程每1秒钟打印1个数字，数字从1开始一直到10，即1.2.3......10
import time
import threading
# def pri():
#     for i in range(1,11):
#         print(i)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     thread = threading.Thread(target=pri)
#     thread.start()


# 1）.创建2个子线程，线程1、2同时对全局变量num各加100万次操作（num初始值为0），每次加1，最后执行完成打印结果，
# （2）.用互斥锁解决上面题目出现的num不是200万的问题
# num=0
# lock = threading.Lock()
# def work1():
#     global num
#     for i in range(1000000):
#         lock.acquire(True)
#         num+=1
#         lock.release()
#     print(num)
# def work2():
#     global num
#     for i in range(1000000):
#         lock.acquire(True)
#         num += 1
#         lock.release()
#     print(num)
# if __name__ == '__main__':
#     thread1=threading.Thread(target=work1)
#     thread2 = threading.Thread(target=work2)
#     thread1.start()
#     thread2.start()

# 创建两个udp程序·，如udpA能接收，udpB发送的数据并·打印出来·
import socket

# if __name__ == '__main__':
#     udpa = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#     udpa.bind(("",8080))
#     msg = input("输入")
#     udpa.sendto(msg.encode("gbk"), ('10.10.24.120',8080))
#     udpa.close()

    # udpb = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # udpb.bind(("", 9999))
    # data,addr = udpb.recvfrom(1024)
    # print(data.decode("gbk"))
    # udpb.close()
# 四.创建一个tcp服务器
# （1）能接收tcp客户端发来的请求
# （2）能并发处理客户端连接
# （3）能接收tcp客户端发来的数据、每次收到数据打印出来并dA回复客户端“已收到！谢谢！”、直到客户端主动断开（线程版）


# def send(t_c_socket):
#     try:
#         while True:
#             msg = input("已收到！谢谢！")
#             t_c_socket.send(msg.encode("gbk"))
#     except Exception as e:
#         print(e)
#     finally:
#         t_c_socket.close()
# def res(t_c_socket):
#     try:
#         while True:
#             data=t_c_socket.recv(1024)
#             print(data.decode("gbk"))
#     except Exception as e:
#         print(e)
#     finally:
#         t_c_socket.close()
# if __name__ == '__main__':
#     tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     tcp_socket.bind(("",7373))
#     tcp_socket.listen(5)
#
#     while True:
#         t_c_socket, addr = tcp_socket.accept()
#         r_thread=threading.Thread(target=res,args=(t_c_socket,))
#         s_thread=threading.Thread(target=send,args=(t_c_socket,))
#         r_thread.start()
#         s_thread.start()

 # 1.场景是有一张圆桌， 5位哲学家围坐圆桌吃饭。 问题是每位哲学家之间的位置只有1根筷子，即圆桌上5位哲学家和5支筷子
# 2.开始吃饭时，每位哲学家首先伸手去拿左手边的筷子，拿到左手边筷子的哲学家，再伸手去抢右手边的筷子。
# 如果两支筷子都抢到，就可以吃一口饭，然后把两只筷子放下，之后进行下一轮；如果没有抢到右手边的筷子，就放下左手边的筷子，此轮不吃饭。如此进行。

