import pygame
from random import randint
import os

os.environ['SDL_VIDEO_WINDOW_POS']="50,50"
pygame.init()

def bounce():
    if 825<=ball.y<=875:
        if stick.x <= ball.x < stick.x+30 and ball.speedY>0:
            boing.play()
            ball.reverseY()
            ball.speedX -= 2
            print("좌측 X{}\tY{}".format(ball.speedX,ball.speedY))
        elif stick.x+30 <= ball.x < stick.x+50 and ball.speedY>0:
            boing.play()
            ball.speedY += 1
            ball.reverseY()
            print("가운데 X{}\tY{}".format(ball.speedX,ball.speedY))
        elif stick.x+50 <= ball.x < stick.x+80 and ball.speedY>0:
            boing.play()
            ball.reverseY()
            ball.speedX += 2
            print("우측 X{}\tY{}".format(ball.speedX,ball.speedY))
    

screen = pygame.display.set_mode((600,900))

boing = pygame.mixer.Sound(r"E:\dev\python_workspace\sounds\Boing.wav")
boing.set_volume(0.5)
wallboing = pygame.mixer.Sound(r"E:\dev\python_workspace\sounds\Bassdrum.wav")
wallboing.set_volume(0.5)

bgimg = pygame.image.load(r"E:\dev\python_workspace\img (2)\space.jpg")

ballimg = pygame.image.load(r"E:\dev\python_workspace\img\gold.png")
class Ball:
    def __init__(self,x=300,y=830):
        self.x = x
        self.y = y
        self.speedX = randint(-5,5)
        self.speedY = randint(1,5)
    def speed(self):
        self.x += self.speedX
        self.y += self.speedY
    def reverseX(self):
        self.speedX *= -1
    def reverseY(self):
        self.speedY *= -1
ball = Ball()

stickimg = pygame.image.load(r"E:\dev\python_workspace\img\stick.png")
class Stick:
    def __init__(self,x=300,y=850):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 15
stick = Stick()

endimg = pygame.image.load(r"E:\dev\python_workspace\img (2)\gameover.jpg")
endimg = pygame.transform.scale(endimg,(600,337))

isRunning = True
isGameOver = False
clock = pygame.time.Clock()
while isRunning:
    fps = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if isGameOver and event.type == pygame.KEYUP:
            if event.key == pygame.K_i:
                isGameOver = False
                ball.x = 300
                ball.y = 400
    #배경
    screen.blit(bgimg,(0,0))
    
    #공
    # if not isGameOver:
    #     ball.speed()
    if ball.x <= 25 or ball.x >=575:
        wallboing.play()
        ball.reverseX()
    if ball.y <= 25:
        wallboing.play()
        ball.reverseY()
    if ball.y >= 900:
        isGameOver = True
    screen.blit(ballimg,(ball.x-25,ball.y-25))
    bounce()


    #막대
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        stick.x -= 5
    if keys[pygame.K_RIGHT]:
        stick.x += 5
    screen.blit(stickimg,(stick.x,stick.y))

    #게임오버
    if isGameOver:
        screen.blit(endimg,(0,300))
    pygame.display.update()
pygame.quit()