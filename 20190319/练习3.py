#很多人在聚餐时都玩过猜数字游戏，由某人随机出一个指定范围内的数，然后其他人一个一个猜，猜的过程中区间不断缩小，直到猜中为止。
class gressCount(object):
    def gress():
        import random
        count = random.randrange(1, 100)#产生一个随机数
        print(count)
        gressCount=int(input('输入一个数：'))
        while gressCount!= count:
            #猜的数比正确答案小了
            if gressCount < count:
                print('小了，请猜一个再大点的数')
                gressCount = int(input('输入一个数：'))
                # 猜的数比正确答案大了
            elif gressCount>count:
                print('大了，请猜一个再小点的数')
                gressCount = int(input('输入一个数：'))
        print('猜对了')
        return count
if __name__ == '__main__':
    gressCount.gress()