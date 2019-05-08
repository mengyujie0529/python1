import  pygame as p
p.init()

window=p.display.set_mode((600,600))
window.fill([255,255,255])

#画圆
p.draw.circle(window,[0,0,0],[50,50],50,0)

while True:
    for e in p.event.get():
        if e.type == p.QUIT:
            exit()
    p.display.update()