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
enemyImg = 'assets/alien.png'
numEnemies = 4


enemies = []
for x in range(numEnemies):
    enemies.append(enemyObj(enemyImg))


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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if e.collidepoint((mouseX, mouseY)):
                print("Alien Clicked")
    
    # Creates Player and reticle
    player(c)

    pygame.display.update()