import pygame
import random
from time import sleep
from pygame import mixer
pygame.init()
screen=pygame.display.set_mode((800,600))
isrunning=True

pygame.display.set_caption('PROTECT THE CEO')
icon =pygame.image.load('man.png')
pygame.display.set_icon(icon)

block=pygame.image.load('block.png')

blockx=300
blocky=375
changex=0
ceo=pygame.image.load('man.png')


girl=pygame.image.load('girl (1).png')
girlx=random.randint(0,770)
girly=100
xchange=2
ychange=2

score=0
font=pygame.font.Font('freesansbold.ttf',24)
def displayScore(score):
    scoreImage=font.render(str(score),True,(255,255,255))
    screen.blit(scoreImage,(10,10))
def gameOver():
    mixer.stop()

    end=mixer.music.load('Bomb-SoundBible.com-891110113.wav')
    mixer.music.play(-1)

    sleep(0.5)
    gfont=pygame.font.Font('freesansbold.ttf',45)
    game=gfont.render("Game Over!",True,(255,255,255))
    screen.blit(game,(275,275))
isGameover=False

background=mixer.music.load('background.wav')
mixer.music.play(-1)
while(isrunning):
    screen.fill((69,69,69))
   
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isrunning=False
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                changex-=4
            if event.key==pygame.K_RIGHT:
                changex+=4
        if event.type==pygame.KEYUP:
            changex=0
    if blockx+changex>546 or blockx+changex<0:
        changex=0
    else: blockx+=changex

    girlx+=xchange
    girly+=ychange


    if(girlx<0):
        xchange=2
    elif girlx>750:
        xchange=-2
    elif girly<0: ychange *=-1
    if girly>=480:
        # print("Game Over")
        isGameover=True
    elif girlx>(blockx + changex) and girlx<(blockx+changex+254) and girly>425:
        ychange*= -1
        score+=1
        sound = mixer.Sound('laser.wav')
        sound.play()
    
    sleep(0.005)
    displayScore(score)
    if(isGameover):
        gameOver()
        # sleep(4)
    else:
        screen.blit(girl,(girlx,girly))
        screen.blit(block,(blockx,blocky))
        screen.blit(ceo,(375,540))
    pygame.display.update()