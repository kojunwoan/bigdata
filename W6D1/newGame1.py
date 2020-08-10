import pygame
from random import randint
import math

def pythagoras(x1,y1,x2,y2):
    return math.dist((x1,y1),(x2,y2))

class Missie:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    # def __del__(self):
    #     print("미사일 제거됨")

class EnemyShip:
    def __init__(self,x,rl,y=-70,hp=5,img=0,type=0):
        self.x = x
        self.rl = rl
        self.y = y
        self.hp = hp
        self.img = img
        self.type = type
    # def __del__(self):
    #     print("적 제거됨")
pygame.init()

pygame.mixer.music.load(r"E:\dev\python_workspace\sounds_space\The Raiden Project OST - Metal Storm.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(1)
screen_width = 600
screen_height = 900

screen = pygame.display.set_mode((screen_width,screen_height))

isRunning = True
pygame.display.set_caption("짭라이덴")

bgimg = pygame.image.load(r"E:\dev\python_workspace\img (2)\space.jpg")
bg1Y = 0
bg2Y = -900

playerimg = [pygame.image.load(r"E:\dev\python_workspace\img (2)\player"+str(i)+".png") for i in range(4)]
cnt = 1
playerX = 300
playerY = 700

misileimg = pygame.image.load(r"E:\dev\python_workspace\img (2)\missile1.png")
misileX = playerX+57/2-5/2
misileY = playerY-19
misileL = []
mcnt = 0

misile2img = pygame.image.load(r"E:\dev\python_workspace\img (2)\missile2.png")
misile2X = playerX+57/2-5/2
misile2Y = playerY-19

enemyimg = [pygame.image.load(r"E:\dev\python_workspace\img (2)\gunship"+str(i)+".png") for i in range(4)] 
enemyL = []

pygame.font.init()
myFont = pygame.font.SysFont("Comic Sans MS",30)
score = 0

endimg = pygame.image.load(r"E:\dev\python_workspace\img (2)\gameover.jpg")
endimg = pygame.transform.scale(endimg,(600,337))
isEnd = False
cleartime = 240

clock = pygame.time.Clock()
while isRunning:
    cnt += 1 
    fps = clock.tick(120)
    keys = pygame.key.get_pressed()
    playerX, playerY = pygame.mouse.get_pos()
    playerX -=57/2
    playerY -=60/2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            misileX = playerX+57/2-5/2
            misileY = playerY-19
            misileL.append(Missie(misileX,misileY))   
    #배경 컨트롤
    bg1Y += 2
    bg2Y += 2
    if bg1Y >= 900:
        bg1Y = -900
    if bg2Y >= 900:
        bg2Y = -900
    screen.blit(bgimg,(0,bg1Y))
    screen.blit(bgimg,(0,bg2Y))

    #미사일 컨트롤
    if keys[pygame.K_z]:
        mcnt += 1
        if mcnt%10 == 0:
            misileX = playerX+57/2-5/2
            misileY = playerY-19
            misileL.append(Missie(misileX,misileY))       
    if cnt%10 == 0:
        misileX = playerX+57/2-5/2
        misileY = playerY-19
        misileL.append(Missie(misileX,misileY))  
    for misile in misileL:
        screen.blit(misileimg,(misile.x,misile.y))
        misile.y -= 6
        if misile.y < -20:
            misileL.remove(misile)

    screen.blit(misile2img,(0,0))

    #적 컨트롤
    if randint(1,150-score) == 1:
        rl = 1
        if randint(0,1):
            rl *= -1
        enemyL.append(EnemyShip(randint(0,543),rl))
    for enemy in enemyL:
        screen.blit(enemyimg[enemy.img%20//5],(enemy.x,enemy.y))
        enemy.x += enemy.rl
        if enemy.x < 0:
            enemy.x = 0
            enemy.rl *= -1
        if enemy.x > screen_width-57:
            enemy.x = screen_width-57
            enemy.rl *= -1
        if score >= 50:
            enemy.y +=1
        if score >= 100:
            enemy.y +=1
        enemy.y += 1
        enemy.img += 1
        if randint(1,100) == 1:
            enemy.rl *= -1
    #적과 미사일 충돌 이벤트
        for misile in misileL:
            if pythagoras(enemy.x+57/2,enemy.y+60/2,misile.x+5/2,misile.y+19/2) < 29:
                misileL.remove(misile)
                enemy.y -= enemy.hp*2
                enemy.hp -= 1
                if enemy.hp == 0:
                    enemyL.remove(enemy)
                    score += 1
        
        if pythagoras(enemy.x+57/2,enemy.y+60/2,playerX+57/2,playerY+60/2) < 58 or enemy.y > 900:
            isEnd = True

    #플레이어 컨트롤
    if keys[pygame.K_LEFT]:
        playerX -= 5
    if keys[pygame.K_UP]:
        playerY -= 5
    if keys[pygame.K_RIGHT]:
        playerX += 5
    if keys[pygame.K_DOWN]:
        playerY += 5
    if playerX < 0:
        playerX = 0
    if playerY < 0:
        playerY = 0
    if playerX > screen_width-57:
        playerX = screen_width-57
    if playerY > screen_height-60:
        playerY = screen_height-60
    screen.blit(playerimg[cnt%20//5],(playerX,playerY))
    txt = myFont.render("SCORE : "+str(score)+"0",False,(255,0,0))
    screen.blit(txt,(250,50))
    if isEnd:
        screen.blit(endimg,(0,300))
        cleartime -= 1
        if cleartime == 0:
            isRunning = False
    pygame.display.update()
pygame.quit()