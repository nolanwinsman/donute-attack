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
SCREEN_WIDTH = 1920  
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Donut Attack")

# Player
playerImg = 'assets/crosshair.png'
player = playerObj(playerImg)

# Sounds
bulletSound = pygame.mixer.Sound('sounds/aturax_tyrepressurerelease_01.wav') # Temp sound

# Enemies
pink_img = 'assets/donut/pink_donut.png'
red_img = 'assets/donut/red_donut.png'
blue_img = 'assets/donut/blue_donut.png'
numEnemies = 10
enemies = pygame.sprite.Group() # list of all the enemies
for x in range(5):
    enemies.add(pink_donut(pink_img))
    enemies.add(red_donut(red_img))
    enemies.add(blue_donut(blue_img))

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
                    # if enemy is clicked
                    if e.collidepoint((player.mouseX, player.mouseY)):
                        e.shot(screen)
                        player.score += 1

        # Background
        screen.fill(color.black)

        # Time
        current_time = pygame.time.get_ticks()
        
        # Ammo Reload
        if current_time - player.reloadTime > 2500 and player.reloading:
            player.ammo = player.maxAmmo
            player.reloading = False

        # HUD
        HUD.update(screen, player)
        ammo_text = "Ammo: " + str(player.ammo)
        HUD.ammo(screen, ammo_text, HUD.ammoX, HUD.ammoY, 32, player.reloading)

        # Enemies
        tempEnemies = enemies
        # enemies.draw(screen)
        enemies.update(screen)
        for e in tempEnemies:
            # e.update(screen)
            if e.alive is False:
                enemies.remove(e)
        if current_time - enemy_spawn_time > 0:
            enemy_spawn_time += random.randint(500, 1000)
            if len(enemies) < 25:
                enemies.add(random_enemy())


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

def random_enemy():
    options = ['pink', 'red', 'blue']
    result = random.choice(options)
    if result == 'red':
        return red_donut(red_img)
    if result == 'blue':
        return blue_donut(blue_img)
    else:
        return pink_donut(pink_img)

            


if __name__ == "__main__":
    game()