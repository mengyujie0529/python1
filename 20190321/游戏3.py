import pygame
import  random
pygame.init()
window=pygame.display.set_mode((400,600))#设置画布大小（x，y）表示宽度，高度
pygame.display.set_caption('cool')#设置画布的名字
# window.fill([255,255,255])#改变背景色
image=pygame.image.load('b.png').convert()#加载背景
imageDown=pygame.image.load('skier_down.png').convert()
imageCrash=pygame.image.load('skier_crash.png').convert()
imageLeft1=pygame.image.load('skier_left1.png').convert()
imageLeft2=pygame.image.load('skier_left2.png').convert()
imageRight1=pygame.image.load('skier_right1.png').convert()
imageRight2=pygame.image.load('skier_right2.png').convert()
imageTree=pygame.image.load('skier_tree.png').convert()
imageFlag=pygame.image.load('skier_flag.png').convert()

pygame.mixer.init()
pygame.mixer.music.load('liangliang.mp3')   #加载音乐
pygame.mixer.music.play()#播放音乐

class Person():#滑雪的人的类
    def __init__(self,personX,personY,ima):
        self.personX=personX
        self.personY=personY
        self.ima=ima
    #向下移动
    def moveDown(self):
        print("向下")
        self.personY += 20
        pygame.time.delay(50)

        self.ima = imageDown
    #向左移动
    def moveLeft(self):
        print("向左")
        self.personX -= 20
        pygame.time.delay(50)
        self.ima = imageLeft1
    #向右移动
    def moveRight(self):
        print("向右")
        self.personX += 20
        pygame.time.delay(50)
        self.ima = imageRight1
    def personAppear(self):
        window.blit(self.ima, (self.personX, self.personY))
    def getX(self):
        return self.personX
    def getY(self):
        return  self.personY


class Tree():
    listTree = []
    def __init__(self,imaTree,treeX,treeY):
        self.imaTree=imaTree
        self.treeX=treeX
        self.treeY=treeY
    #随机位置出现树
    def randomAppear(self):
        treeNum=5
        # for i in range(treeNum):
        #     tree=window.blit(self.imaTree, (self.treeX, self.treeY))
        #     listTree.append(tree)
        tree=window.blit(self.imaTree, (self.treeX, self.treeY))
        # while self.treeY > 0:
        #     pygame.time.delay(50)
        #     pygame.draw.rect(window, [255, 255, 255], [self.treeX, self.treeY, 42, 48])
        #     self.treeY -= 5
        #     window.blit(self.imaTree, (self.treeX, self.treeY))
        #     pygame.display.flip()


ming=Person(180,20,imageDown)
tree1=Tree(imageTree,random.randint(0,window.get_width()-42),random.randint(0,window.get_height()-42))
while True:
    window.blit(image,(0,0))#把图片添加到画布
    #window.blit(imageDown,(personX,personY))#人物初始位置在（180，0）
    ret=pygame.event.get()

    isPress = pygame.key.get_pressed()#bool :True
    if isPress[pygame.K_a] == True or isPress[pygame.K_LEFT] == True:
        if ming.personX > 0:
            # print("向左")
            # personX -= 20
            # pygame.time.delay(150)
            # ima = imageLeft1
            ming.moveLeft()

    elif isPress[pygame.K_s]== True or isPress[pygame.K_DOWN]== True:
        if ming.personY < window.get_height()-64:
            # print("向下")
            # personY += 20
            # pygame.time.delay(150)
            # ima = imageDown
            ming.moveDown()
    elif isPress[pygame.K_d]== True or isPress[pygame.K_RIGHT]== True:
        if ming.personX < window.get_width()-30:
            # print("向右")
            # personX += 20
            # pygame.time.delay(150)
            # ima = imageRight1
            ming.moveRight()
    for obj in ret:
        if obj.type == pygame.QUIT:#关闭窗口
            exit()

    ming.personAppear()

    tree1.randomAppear()
    pygame.display.update() #刷新  *必须要刷新，不然就不会显示