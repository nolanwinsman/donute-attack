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
player = playerObj()

# Enemies
enemyImg = 'assets/alien.png'
numEnemies = 4
enemies = [] # list of all the enemies
for x in range(5):
    enemies.append(enemyObj(enemyImg))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        player.color = colors.red
        player.mouseX, player.mouseY = pygame.mouse.get_pos() #mouse x,y cordinates
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            player.color = colors.white
            for e in enemies: #might find a way to do this without looping
                if e.collidepoint((player.mouseX, player.mouseY)):
                    e.health -= 1
                    player.score += 1
    
    screen.fill(colors.darkBlue)
    
    # Updates the enemies
    for e in enemies:
        e.update(screen)

    # Creates Player and reticle
    player.update(screen)
    pygame.display.update()