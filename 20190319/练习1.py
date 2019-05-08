#谁是卧底也是深受很多人喜欢的游戏，起码要三人以上才能玩，大致分为几个阶段：
# 1.分配平民词语和卧底词语--->
# 2.玩家依次发言--->
# 3.根据发言投票认为谁是卧底--->
# 4.得到票数最多的玩家出局--->
# 5.出局玩家刚好是卧底则平民胜利，如果出局玩家是平民则被冤死并继续第2步，当剩下的平民只有1个时卧底胜利。
# 特殊情况是，出现两名或以上的玩家票数相同，则相同票数的玩家重新发言，然后全体针对这几个玩家投票。
class Person(object):
    def __init__(self,word):
        self.word=word

    def say(self):#发言
        print('我要说：',self.word)
    def touPiao(self):#投票
        print('我要投票：')

if __name__ == '__main__':
    p1=Person('a')
    p2 = Person('a')
    p3 = Person('b')
    #依次发言
    p1.say()
    p2.say()
    p3.say()