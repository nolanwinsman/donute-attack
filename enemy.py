import pygame
from PIL import Image
from data import screen
import math
import random

class enemyObj(object):
    def __init__(self, img):
        self.screenData = screen()
        self.length, self.height = Image.open(img).size
        self.x = random.randint(math.floor(self.screenData.width/100), self.screenData.width-math.floor(self.screenData.width/50))
        self.y = random.randint(math.floor(self.screenData.height/100), self.screenData.height-math.floor(self.screenData.height/4))
        self.img = pygame.image.load(img)
        self.deltaX = 0.5
        self.deltaY = -0.5
        self.health = 1
        self.alive = True
    
    def update(self, win):
        if self.health >= 1:
            self.draw(win)
        else: 
            self.alive = False

    def move(self):
        # If the enemy is touching the left or right border
        if self.x >= self.screenData.width - math.floor(self.screenData.width/100) or self.x <= 0 + math.floor(self.screenData.width/100):
            self.deltaX *= -1
        # If the enemy is touching the top or bottom border
        if self.y >= self.screenData.height - math.floor(self.screenData.height/4) or self.y <= 0:
            self.deltaY *= -1
        self.x += self.deltaX
        self.y += self.deltaY

    def draw(self, win):
        self.move()
        win.blit(self.img, (self.x, self.y))

    # If the enemy is clicked
    def collidepoint(self, point):
        return pygame.Rect(self.x, self.y, self.length, self.height).collidepoint(point)