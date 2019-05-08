#电视节目中的”你来比划我来猜“大家应该都看过，而且很多人也玩过，
# 规则就是一个人看词语比划相应动作和说一些提示，另一个人看不到词语要通过比划的动作猜出来，猜的过程中主持人判断是否符合规则。
class Game2(object):
    word=input('输入一个词语：')#word是需要回答的正确答案
    flag=False#判断回答正确与否
    while flag==False:
        answer=input("输入回答：")
        #如果回答错误就一直重新猜
        if answer != word:
            flag=False
            print("回答错误，重新猜！")
        else:#回答正确，跳出循环
            flag=True
            print("回答正确！")
            break

