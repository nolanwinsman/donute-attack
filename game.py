import pygame
from data import *
from enemy import *
from player import *
from hud import *
import random
import math
import time
import sys




pygame.init()

colors = colors()
screenData = screen()

# Time
clock = pygame.time.Clock()
current_time = 0
button_press_time = 0

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

# HUD
HUD = hud()


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        player.color = colors.red
        player.mouseX, player.mouseY = pygame.mouse.get_pos() #mouse x,y cordinates
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Player Reloads Weapon
            if event.key == pygame.K_r or event.key == pygame.K_SPACE:
                player.reloadTime = pygame.time.get_ticks()
                player.reloading = True
        if event.type == pygame.MOUSEBUTTONUP and player.ammo > 0:
            player.color = colors.white
            player.height, player.length = 11, 11
            player.ammo -= 1
            for e in enemies: #might find a way to do this without looping
                if e.collidepoint((player.mouseX, player.mouseY)):
                    e.health -= 1
                    player.score += 1
    # Time
    current_time = pygame.time.get_ticks()
    
    # Ammo Reload
    if current_time - player.reloadTime > 2500 and player.reloading:
        player.ammo = player.maxAmmo
        player.reloading = False

    
    screen.fill(colors.darkBlue)
    HUD.update(screen)
    # self, win, text, x, y, fontSize
    ammoText = "Ammo: " + str(player.ammo)
    HUD.ammo(screen, ammoText, HUD.ammoX, HUD.ammoY, 32, player.reloading)


    # Updates the enemies
    for e in enemies:
        e.update(screen)

    # Creates Player and reticle
    player.update(screen)
    pygame.display.update()