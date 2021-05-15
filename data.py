import pygame
import math
import random

class colors:
    def __init__(self):
        # Define Colors
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.blue = pygame.Color(0, 0, 255)
        self.darkBlue = pygame.Color(0, 0, 128)
        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)
        self.pink = pygame.Color(255, 200, 200)
        self.yellow = pygame.Color(255, 255, 0)

class screen:
    def __init__(self):
        # Define Screen
        self.width = 1600
        self.height = 900

class enemy(object):
    def __init__(self, x, y, screen, img):
        self.x = x
        self.y = y
        self.velocity = 1
        self.img = img
        self.deltaX = 0.3
        self.deltaY = -0.3
    
    def move(self):
        screenData = screen()
        if self.x >= screenData.width - math.floor(screenData.width/100) or self.x <= 0 + math.floor(screenData.width/100):
            self.deltaX *= -1
        if self.y >= screenData.height - math.floor(screenData.height/4) or self.y <= 0:
            self.deltaY *= -1
        self.x += self.deltaX
        self.y += self.deltaY


    def draw(self, screen):
        self.move()
        screen.blit(self.img, (self.x, self.y))

