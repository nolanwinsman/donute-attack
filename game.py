import pygame
import time
from data import *
import random
import math

pygame.init()

colors = colors()
screenData = screen()

# Screen
SCREEN_WIDTH = screenData.width
SCREEN_HEIGHT = screenData.height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Light Gun Game")



# Player
def player(color):
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) #hides the mouse
    pygame.draw.rect(screen, color, (mouseX, mouseY, 10, 10)) #creates reticle


# Enemies
enemyImg = pygame.image.load('assets/alien.png')
numEnemies = 4

# Two random x, y cords withing the boundaries set.
def enemyPlacements():
        x = random.randint(SCREEN_WIDTH/100, SCREEN_WIDTH-math.floor(SCREEN_WIDTH/50))
        y = random.randint(SCREEN_HEIGHT/100, SCREEN_HEIGHT-math.floor(SCREEN_HEIGHT/4))
        return x, y


enemies = []
for x in range(numEnemies):
    x, y = enemyPlacements()
    enemies.append(enemy(x, y, screen, enemyImg))


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        c = colors.red
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            c = colors.white
    
    screen.fill(colors.darkBlue)
    mouseX, mouseY = pygame.mouse.get_pos() #mouse x,y cordinates
    bottom_border = SCREEN_HEIGHT-math.floor(SCREEN_HEIGHT/4)
    #pygame.draw.line(screen, colors.white, (SCREEN_WIDTH, 0), (800, 800), 5)
    
    # Creates the enemies
    for e in enemies:
        e.draw(screen)
    
    # Creates Player and reticle
    player(c)

    pygame.display.update()