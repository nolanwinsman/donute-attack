import pygame
import time
from data import *
from enemy import *
from player import *
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
for x in range(10):
    enemies.append(enemyObj(enemyImg))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        c = colors.red
        mouseX, mouseY = pygame.mouse.get_pos() #mouse x,y cordinates
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            c = colors.white
            for e in enemies: #might find a way to do this without looping
                if e.collidepoint((mouseX, mouseY)):
                    e.health -= 1
    screen.fill(colors.darkBlue)
    # Updates the enemies
    for e in enemies:
        e.update(screen)

    
    # Creates Player and reticle
    player(c)

    pygame.display.update()