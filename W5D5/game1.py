import pygame
import math
def pythagoras(x1,y1,x2,y2):
    return math.dist((x1,y1),(x2,y2))

pygame.init()

pygame.mixer.music.load(r"e:\dev\python_workspace\sounds\backsound.mp3")
pygame.mixer.music.set_volume(0.5) # 1~0.1
pygame.mixer.music.play(1)

fsound = pygame.mixer.Sound(r"e:\dev\python_workspace\sounds\fire.wav")
fsound.set_volume(0.5) # 1~0.1
ssound = pygame.mixer.Sound(r"e:\dev\python_workspace\sounds\scream.wav")
ssound.set_volume(0.5) # 1~0.1

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("hunt")
bg1 = pygame.image.load(r'e:\dev\python_workspace\img\bg.jpg')
bg2 = pygame.image.load(r'e:\dev\python_workspace\img\bg.jpg')
bg1x = 0
bg2x = 1404
rw = 75
rh = 96
rx = 500
ry = 200
rabbit1img = pygame.image.load(r'E:\dev\python_workspace\img\rabbit1.png')
rabbit2img = pygame.image.load(r'E:\dev\python_workspace\img\rabbit2.png')
rabbit1 = pygame.transform.scale(rabbit1img,(rw,rh))
rabbit2 = pygame.transform.scale(rabbit2img,(rw,rh))

snipe = pygame.image.load(r'E:\dev\python_workspace\img\snipe2.png')
snipe = pygame.transform.scale(snipe,(74,74))
snix = 300
sniy = 300

hole = pygame.image.load(r'E:\dev\python_workspace\img\hole.png')
hole = pygame.transform.scale(hole,(16,16))
holex = 2000
holey = 2000
# rsize = 100

clock = pygame.time.Clock()
cnt = 0
isRunning = True
while isRunning:
    cnt += 2
    bg1x -= 4
    bg2x -= 4
    rw = int(75*(1+ry/400))
    rh = int(96*(1+ry/400))
    if bg1x <= -1404:
        bg1x = 1404
    if bg2x <= -1404:
        bg2x = 1404
    fps = clock.tick(60)
    #print("fps :",clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         rx -=5
        #     elif event.key == pygame.K_UP:
        #         ry -=5
        #     elif event.key == pygame.K_RIGHT:
        #         rx +=5
        #     elif event.key == pygame.K_DOWN:
        #         ry +=5
        if event.type == pygame.MOUSEBUTTONUP:
            holex,holey = pygame.mouse.get_pos()
            fsound.play()
            if pythagoras(rx+rw/2,ry+rh*2/3,holex,holey) < 50:
                ssound.play()
            print(pythagoras(rx+rw/2,ry+rh*2/3,holex,holey))
    snix,sniy = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rx -=5
        cnt -= 1
        if rx <= 0:
            rx = 0
    if keys[pygame.K_UP]:
        ry -=5
        cnt += 1
        if ry <= 0:
            ry = 0
        # rsize -= 1
        # rabbit1 = pygame.transform.scale(rabbit1img,(rw*rsize//100,rh*rsize//100))
        # rabbit2 = pygame.transform.scale(rabbit1img,(rw*rsize//100,rh*rsize//100))
        
    if keys[pygame.K_RIGHT]:
        rx +=5
        cnt += 2
        if rx >= screen_width - rw:
            rx = screen_width - rw
    if keys[pygame.K_DOWN]:
        ry +=5
        cnt += 1
        if ry >= screen_height - rh:
            ry = screen_height - rh
        # rsize += 1
        # rabbit1 = pygame.transform.scale(rabbit1img,(rw*rsize//100,rh*rsize//100))
        # rabbit2 = pygame.transform.scale(rabbit1img,(rw*rsize//100,rh*rsize//100))

    if keys[pygame.K_1]:
        pygame.mixer.music.play()
    if keys[pygame.K_2]:
        pygame.mixer.music.stop()
    
    screen.blit(bg1,(bg1x,0))
    screen.blit(bg2,(bg2x,0))
    if cnt%20<10:
        rabbit1 = pygame.transform.scale(rabbit1img,(rw,rh))
        screen.blit(rabbit1,(rx,ry))
    else:
        rabbit2 = pygame.transform.scale(rabbit2img,(rw,rh))
        screen.blit(rabbit2,(rx,ry))
    screen.blit(hole,(holex-8,holey-8))
    screen.blit(snipe,(snix-37,sniy-37))
    pygame.display.update()

pygame.quit()