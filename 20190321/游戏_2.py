import pygame
window=pygame.display.set_mode((400,600))#设置画布大小（x，y）表示宽度，高度
pygame.display.set_caption('cool')#设置画布的名字

image=pygame.image.load('a.jpg').convert()#加载背景
imageDown=pygame.image.load('skier_down.png').convert()
imageCrash=pygame.image.load('skier_crash.png').convert()
imageLeft1=pygame.image.load('skier_left1.png').convert()
imageLeft2=pygame.image.load('skier_left2.png').convert()
imageRight1=pygame.image.load('skier_right1.png').convert()
imageRight2=pygame.image.load('skier_right2.png').convert()

pygame.mixer.init()
pygame.mixer.music.load('liangliang.mp3')   #加载音乐
pygame.mixer.music.play()#播放音乐

personX=180
personY=0
ima=imageDown
while True:
    window.blit(image,(0,0))#把图片添加到画布
    #window.blit(imageDown,(personX,personY))#人物初始位置在（180，0）

    ret=pygame.event.get()


    isPress = pygame.key.get_pressed()
    if isPress[pygame.K_a] == True or isPress[pygame.K_LEFT] == True:
        if personX > 0:
            print("向左")
            personX -= 20
            pygame.time.delay(150)
            ima = imageLeft1

    elif isPress[pygame.K_s]== True or isPress[pygame.K_DOWN]== True:
        if personY < window.get_height()-64:
            print("向下")
            personY += 20
            pygame.time.delay(150)
            ima = imageDown
    elif isPress[pygame.K_d]== True or isPress[pygame.K_RIGHT]== True:
        if personX < window.get_width()-30:
            print("向右")
            personX += 20
            pygame.time.delay(150)
            ima = imageRight1


    for obj in ret:
        if obj.type == pygame.QUIT:#关闭窗口
            print("退出")
            exit()
    window.blit(ima, (personX, personY))  # 人物初始位置在（180，0）


    pygame.display.update() #刷新  *必须要刷新，不然就不会显示