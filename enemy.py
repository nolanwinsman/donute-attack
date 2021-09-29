import pygame
from PIL import Image
from data import screen
import math
import random

class enemyObj(object):
    def __init__(self, img):
        self.screenData = screen()

        #Random coordinates for where they spawn
        self.x = random.randint(math.floor(self.screenData.width/100), self.screenData.width-math.floor(self.screenData.width/50))
        self.y = random.randint(math.floor(self.screenData.height/100), self.screenData.height-math.floor(self.screenData.height/4))
        
        #Sets the image and scales it
        self.img = pygame.image.load(img)
        self.length, self.height = Image.open(img).size
        self.length, self.height = self.length*5, self.height*5
        self.img = pygame.transform.scale(self.img, (self.length, self.height))
        
        
        #Affects how fast the sprite moves
        self.deltaX = 1.5
        self.deltaY = -1.5
        
        #Health
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

    # displays the image of the sprite
    def draw(self, win):
        self.move()
        win.blit(self.img, (self.x, self.y))

    # If the enemy is clicked
    def collidepoint(self, point):
        return pygame.Rect(self.x, self.y, self.length, self.height).collidepoint(point)