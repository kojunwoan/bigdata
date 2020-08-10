import pygame
import math
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

gogun = [pygame.transform.scale(run,(gw,gh)) for run in [pygame.image.load(r"E:\dev\python_workspace\img\run"+str(i+1)+".png") for i in range(4)]]

goldimg = pygame.image.load(r"E:\dev\python_workspace\img\gold.png")
silverimg = pygame.image.load(r"E:\dev\python_workspace\img\silver.png")
gold = []
silver = []

clock = pygame.time.Clock()
cnt = 0
jump = False
jumpcnt = 0
isRunning = True

while isRunning:
    cnt += 1
    bg0x -= 3
    bg1x -= 3
    if bg0x <= -800:
        bg0x = 800
    if bg1x <= -800:
        bg1x = 800
    fps = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jump:
                jump = True
                jumpcnt = -10
        
    screen.blit(bg[0],(bg0x,0))
    screen.blit(bg[1],(bg1x,0))
    gy += jumpcnt
    if jump:
        jumpcnt += 0.25
    if jumpcnt > 10:
        jumpcnt = 0
        jump = False
    screen.blit(gogun[cnt%20//5],(50,int(gy)))
    if randint(1,40) == 1:
        gold.append([800,randint(1,5)*50+50])
    if randint(1,40) == 1:
        silver.append([800,randint(1,5)*50+50])
    for gol in gold:
        screen.blit(goldimg,(gol[0],gol[1]))
        gol[0] -= 3
        if gol[0] < -50:
            gold.remove(gol)
        if pythagoras(50+gw/2,gy+gh/2,gol[0]+25,gol[1]+25) <= 50:
            gold.remove(gol)      
    for sil in silver:
        screen.blit(silverimg,(sil[0],sil[1]))
        sil[0] -= 3
        if sil[0] < -50:
            silver.remove(sil)
        if pythagoras(50+gw/2,gy+gh/2,sil[0]+27,sil[1]+27) <= 50:
            silver.remove(sil)            
    pygame.display.update()

pygame.quit()