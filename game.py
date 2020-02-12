import pygame
import time
import random

windowX = 800
windowY = 800
screen = pygame.display.set_mode((windowX,windowY))
clock = pygame.time.Clock()
hearts = [pygame.image.load('heart.png'),pygame.image.load('heart.png'),pygame.image.load('heart.png'),pygame.image.load('heart.png')]
gameOver = pygame.image.load('gameOver.png')
questions = [pygame.image.load('questions/q1.png'),pygame.image.load('questions/q2.png'),pygame.image.load('questions/q3.png'),pygame.image.load('questions/q4.png'),pygame.image.load('questions/q5.png'),pygame.image.load('questions/q6.png'),pygame.image.load('questions/q7.png'),pygame.image.load('questions/q8.png')]
p1 = pygame.image.load('p1.png')
health = 2

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.hitbox = (self.x-2, self.y, self.width+3, self.height)
        
    def draw(self, screen):
        screen.blit(p1,(self.x,self.y))
        self.hitbox = (self.x-2, self.y, self.width+3, self.height)
        self.move(screen)
    
    def move(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x < windowX - self.width - self.vel:
            self.x += self.vel
        if keys[pygame.K_UP] and self.y > 500:
            self.y -= self.vel
        if keys[pygame.K_DOWN] and self.y < windowY - self.height - self.vel:
            self.y += self.vel

class Projectiles(object):
    def __init__(self, x, y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 30
    def draw(self,screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius,1)
        
        
class Enemy(object):
    def __init__(self,x,y,width,height,correct,picture):
        self.x = x
        self.y = y
        self.picture = picture
        self.width = width
        self.height = height
        self.velX = random.randrange(3,8)
        self.velY = random.randrange(3,8)
        self.correct = correct
        self.pathX = [100,700]
        self.pathY = [20,500]
        self.hitbox = (self.x,self.y,self.width,self.height)
    def draw(self, screen):
        self.hitbox = (self.x,self.y,self.width,self.height)
        screen.blit(self.picture,(self.x,self.y))
        self.move()
        self.hit()
    def move(self):
        self.x+=self.velX
        self.y+=self.velY
        if self.x < self.pathX[0]:
            self.velX*=-1
        if self.x + self.width > self.pathX[1]:
            self.velX*=-1
        if self.y < self.pathY[0]:
            self.velY*=-1
        if self.y + self.height > self.pathY[1]:
            self.velY*=-1
    def hit(self):
        global health
        global count
        global amount
        for bullet in bullets:
            if bullet.y - bullet.radius < self.hitbox[1] + self.hitbox[3] and bullet.y + bullet.radius > self.hitbox[1]:
                if bullet.x - bullet.radius < self.hitbox[0] + self.hitbox[2] and bullet.x + bullet.radius > self.hitbox[0]:
                    if self.correct:
                        count+=1
                        amount = 1
                    else:
                        health-=1
                    bullets.pop(bullets.index(bullet))
            
    
mercury = Enemy(500,200,100,100,False,pygame.image.load('planets/1_mercury.png'))
venus = Enemy(300,150,100,100,False,pygame.image.load('planets/2_venus.png'))
earth = Enemy(600,300,100,100,False,pygame.image.load('planets/3_earth.png'))
mars = Enemy(400,350,100,100,False,pygame.image.load('planets/4_mars.png'))
jupiter = Enemy(450,100,100,100,False,pygame.image.load('planets/5_jupiter.png'))
saturn = Enemy(100,370,100,100,False,pygame.image.load('saturn.png'))
uranus = Enemy(100,100,100,100,False,pygame.image.load('planets/7_uranus.png'))
neptune = Enemy(600,400,100,100,False,pygame.image.load('planets/8_neptune.png'))

gameos = pygame.image.load('gameOver.png')
def screen1():
    btb=0
    screen.blit(gameos,(0,0))
    while btb != 2000:
        btb+=1
        pygame.display.update()
        
def winScreen():
    bt=0
    screen.blit(pygame.image.load('winScreen.png'),(0,40))
    while bt != 2000:
        bt+=1
        pygame.display.update()

amount = 1
def levelOne():
    global count
    global amount
    if count == 1:
        screen.blit(questions[0],(0,700))
    if count == 1 and amount > 200:
        jupiter.correct = True
        neptune.correct = False
        saturn.correct = False
        level1 = [jupiter,neptune,saturn]
        for i in level1:
            i.draw(screen)
def levelTwo():
    global count
    global amount
    if count == 2:
        screen.blit(questions[1],(0,700))
    if count == 2 and amount > 200:
        uranus.correct = True
        mercury.correct = False
        venus.correct = False
        level2 = [uranus,mercury,venus]
        for i in level2:
            i.draw(screen)
def levelThree():
    global count
    global amount
    if count == 3:
        screen.blit(questions[2],(0,700))
    if count == 3 and amount > 200:
        mars.correct = True
        neptune.correct = False
        level3 = [mars,mercury,neptune]
        for i in level3:
            i.draw(screen)
def levelFour():
    global count
    global amount
    if count == 4:
        screen.blit(questions[3],(0,700))
    if count == 4 and amount > 260:
        venus.correct = True
        earth.correct = False
        mars.correct = False
        level4 = [venus,earth,mars]
        for i in level4:
            i.draw(screen)
def levelFive():
    global count
    global amount
    if count == 5 and amount < 200:
        screen.blit(questions[4],(0,700))
    if count == 5 and amount > 200:
        saturn.correct = True
        uranus.correct = False
        neptune.correct = False
        level5 = [saturn,uranus,neptune]
        for i in level5:
            i.draw(screen)
def levelSix():
    global count
    global amount
    if count == 6:
        screen.blit(questions[5],(0,700))
    if count == 6 and amount > 200:
        earth.correct = True
        venus.correct = False
        mercury.correct = False
        level6 = [earth,venus,mercury]
        for i in level6:
            i.draw(screen)
def levelSeven():
    global count
    global amount
    if count == 7:
        screen.blit(questions[6],(0,700))
    if count == 7 and amount > 200:
        neptune.correct = True
        earth.correct = False
        venus.correct = False
        level7 = [neptune,earth,venus]
        for i in level7:
            i.draw(screen)
def levelEight():
    global count
    global amount
    if count == 8:
        screen.blit(questions[7],(0,700))
    if count == 8 and amount > 200:
        mercury.correct = True
        mars.correct = False
        jupiter.correct = False
        level8 = [jupiter,mercury,mars]
        for i in level8:
            i.draw(screen)
            
        
def redrawGameWindow(l):
    screen.fill((0,0,0))
    player.draw(screen)
    if l >= 2:
        screen.blit(hearts[2],(77,7))
    if l >= 1:
        screen.blit(hearts[1],(42,7))
    if l >= 0:
        screen.blit(hearts[0],(7,7))
    for bullet in bullets:
        bullet.draw(screen)
    levelOne()
    levelTwo()
    levelThree()
    levelFour()
    levelFive()
    levelSix()
    levelSeven()
    levelEight()

player = Player(400, 650, 90, 65)
count = 1
#game loop
bullets=[]
def game():
    global health
    global count
    global amount
    shootSound = pygame.mixer.Sound("efx/shoot.wav")
    health = 2
    count = 1
    amount = 1
    while True:
        clock.tick(60)
        amount += 1
        keys = pygame.key.get_pressed()
        for bullet in bullets:
            if bullet.y < windowY and bullet.y > -10:
                bullet.y -= bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        for event in pygame.event.get():
            if keys[pygame.K_z]:
                if len(bullets) <1:
                    shootSound.play()
                    bullets.append(Projectiles(round(player.x+player.width//2),round(player.y - 5),6,(120,30,160)))
            if event.type == pygame.QUIT:
                pygame.quit()
        redrawGameWindow(health)
        if health < 0:
            redrawGameWindow(health)
            screen1()
            break
        if count > 8:
            winScreen()
            break
        pygame.display.update()