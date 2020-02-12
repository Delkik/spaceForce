import pygame
import time
import random
from game import game

#initialize game
pygame.init()
windowX = 800
windowY = 800
screen = pygame.display.set_mode((windowX,windowY))
clock = pygame.time.Clock()

#Title and Icon
pygame.display.set_caption("SPACE FORCE")
pygame.display.set_icon(pygame.image.load('spaceForce.png'))
imgCount = 0
titleScreen1 = [pygame.image.load('title.png'),pygame.image.load('title.png'),pygame.image.load('title.png'),pygame.image.load('title.png'),pygame.image.load('title2.png'),pygame.image.load('title2.png'),pygame.image.load('title2.png'),pygame.image.load('title2.png'),pygame.image.load('title2.png'),pygame.image.load('title2.png')]

#title screen
def title(x,y):
    global imgCount
    if imgCount + 1 >= 9:
        imgCount = 0
    screen.blit(titleScreen1[imgCount],(x,y))
    imgCount+=1

#TitleLoop
def screen0():
    titleS = True
    while titleS:
        clock.tick(7)
        title(0,0)
        pygame.display.update()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                titleS=False
            if event.type == pygame.QUIT:
                pygame.quit()
                
    
while True:
    screen0()
    game()
pygame.quit()
