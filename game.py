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

# Colors
color = colors()

# Time
clock = pygame.time.Clock()
current_time = 0
button_press_time = 0

# Screen
screenData = screen()
# SCREEN_WIDTH = screenData.width
# SCREEN_HEIGHT = screenData.height
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Light Gun Game")

# Player
playerImg = 'assets/crosshair.png'
player = playerObj(playerImg)

# Sounds
# TODO create sound class
bulletSound = pygame.mixer.Sound('sounds/aturax_tyrepressurerelease_01.wav') # Temp sound

# Enemies
enemyImg = 'assets/Donut.png'
numEnemies = 10
enemies = [] # list of all the enemies
for x in range(5):
    enemies.append(enemyObj(enemyImg))



# HUD
HUD = hud()

# Pause
Pause = pause()

# Game Loop
def game():
    running = True
    enemy_spawn_time = random.randint(500, 2000)
    while running:
        for event in pygame.event.get():
            player.color = color.red
            player.mouseX, player.mouseY = pygame.mouse.get_pos() #mouse x,y cordinates
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Press Esc to close game
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Player Reloads Weapon
                elif event.key == pygame.K_r or event.key == pygame.K_SPACE:
                    player.reloadTime = pygame.time.get_ticks()
                    player.reloading = True
                elif event.key == pygame.K_p:
                    Pause.paused = not Pause.paused # toggles the boolean
                    options()
            # Mouse click
            if event.type == pygame.MOUSEBUTTONUP and player.ammo > 0 and not player.reloading:
                player.singleShot()
                bulletSound.play()
                # Check if any enemies are clicked
                for e in enemies:
                    if e.collidepoint((player.mouseX, player.mouseY)):
                        e.health -= 1
                        player.score += 1

        # Time
        current_time = pygame.time.get_ticks()
        
        # Ammo Reload
        if current_time - player.reloadTime > 2500 and player.reloading:
            player.ammo = player.maxAmmo
            player.reloading = False

        # Background
        screen.fill(color.darkBlue)
        
        # HUD
        HUD.update(screen, player)
        ammoText = "Ammo: " + str(player.ammo)
        HUD.ammo(screen, ammoText, HUD.ammoX, HUD.ammoY, 32, player.reloading)

        # Enemies
        tempEnemies = enemies
        for e in tempEnemies:
            e.update(screen)
            if e.health <= 0:
                enemies.remove(e)
        if current_time - enemy_spawn_time > 0:
            enemy_spawn_time += random.randint(500, 2000)
            enemies.append(enemyObj(enemyImg))


        # Player/Reticle
        player.update(screen)
        pygame.display.update()

# The pause menu
def options():
    running = True
    while running:
        for event in pygame.event.get():
            player.mouseX, player.mouseY = pygame.mouse.get_pos() #mouse x,y cordinates
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                    # Press Esc to close game
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # Player Reloads Weapon
                    elif event.key == pygame.K_p:
                        Pause.paused = not Pause
                        running = False
    
        screen.fill(color.blue)
        # Player/Reticle
        Pause.draw(screen)
        player.update(screen)
        pygame.display.update()
            


if __name__ == "__main__":
    game()