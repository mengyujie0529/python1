import pygame

skier_images = ['./skier_crash.png','./skier_down.png','./skier_left1.png','./skier_left2.png','./skier_right1.png','./skier_right2.png']


window=pygame.display.set_mode((400,600))#设置画布大小（x，y）表示宽度，高度
pygame.display.set_caption('cool')#设置画布的名字
image=pygame.image.load('a.jpg').convert()#加载背景

skier = pygame.image.load(skier_images[1]).convert()

pygame.mixer.init()
pygame.mixer.music.load('liangliang.mp3')   #加载音乐
pygame.mixer.music.play()#播放音乐
x = 185
y = 20
while True:
    window.blit(image,(0,0))#把图片添加到画布

    window.blit(skier,(x,y))


    pygame.key.get_pressed()
    ret = pygame.event.get()
    for obj in ret:
        if obj.type == pygame.QUIT:#关闭窗口
            print("退出")
            exit()
        elif obj.type == pygame.KEYDOWN:
            if obj.key==pygame.K_a or obj.key==pygame.K_LEFT:
                print("向左")
                x=x-1
                #skier=skier_images[2]
            elif obj.key==pygame.K_s or obj.key==pygame.K_DOWN:
                print("向下")
                y=y+1
                #skier = skier_images[1]
            elif obj.key==pygame.K_d or obj.key==pygame.K_RIGHT:
                print("向右")
                x=x+1
                #skier = skier_images[4]



    pygame.display.update() #刷新  *必须要刷新，不然就不会显示