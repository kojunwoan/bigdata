import pygame
from random import randint
def pythagoras(x1,y1,x2,y2):
    return math.dist((x1,y1),(x2,y2))
pygame.init()

screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("고군분투")

bg = [pygame.image.load(r"E:\dev\python_workspace\img\bg"+str(i)+".jpg") for i in range(1,3)]
bg0x = 0
bg1x = 800

gw, gh = 100, 110
gy = 270

gogun = [pygame.transform.scale(run,(gw,gh)) for run in [pygame.image.load(r"E:\dev\python_workspace\img\run"+str(i+1)+".png") for i in range(3)]]

goldimg = pygame.image.load(r"E:\dev\python_workspace\img\gold.png")
silverimg = pygame.image.load(r"E:\dev\python_workspace\img\silver.png")
gold = []
silver = []

clock = pygame.time.Clock()
cnt = 0
isRunning = True

while isRunning:
    cnt += 1
    bg0x -= 2
    bg1x -= 2
    if bg0x <= -800:
        bg0x = 800
    if bg1x <= -800:
        bg1x = 800
    fps = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.K_SPACE:
            pass
    
    screen.blit(bg[0],(bg0x,0))
    screen.blit(bg[1],(bg1x,0))
    if cnt%20 < 5:
        screen.blit(gogun[0],(50,gy))
    elif 5<= cnt%20 < 10 or 15<= cnt%20 < 20 :
        screen.blit(gogun[1],(50,gy))
    else:
        screen.blit(gogun[2],(50,gy))
    if randint(1,50) == 1:
        gold.append([800,randint(1,5)*50+50])
    if randint(1,50) == 1:
        silver.append([800,randint(1,5)*50+50])
    for gol in gold:
        screen.blit(goldimg,(gol[0],gol[1]))
        gol[0] -= 2
        if gol[0] < -50:
            gold.remove(gol)
        print(gold)
    for sil in silver:
        screen.blit(silverimg,(sil[0],sil[1]))
        sil[0] -= 2
        if sil[0] < -50:
            silver.remove(sil)
        print(silver)
    pygame.display.update()

pygame.quit()