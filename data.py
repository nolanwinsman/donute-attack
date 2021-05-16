import pygame
import math
import random
from PIL import Image

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

class playerObj(object):
    def __init__(self):
        self.score = 0

    def increaseScore(self, s):
        self.score += s

class enemyObj(object):
    def __init__(self, img):
        self.screenData = screen()
        self.length, self.height = Image.open(img).size
        self.x = random.randint(self.screenData.width/100, self.screenData.width-math.floor(self.screenData.width/50))
        self.y = random.randint(self.screenData.height/100, self.screenData.height-math.floor(self.screenData.height/4))
        self.img = pygame.image.load(img)
        self.deltaX = 0.3
        self.deltaY = -0.3
        self.health = 1
        self.alive = True
    
    def update(self, win):
        if self.health >= 1:
            self.draw(win)
        else:
            self.alive = False

    def move(self):
        if self.x >= self.screenData.width - math.floor(self.screenData.width/100) or self.x <= 0 + math.floor(self.screenData.width/100):
            self.deltaX *= -1
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