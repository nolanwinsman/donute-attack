import pygame
from data import *
from player import *
import math
import random


class hud:
    def __init__(self):
        self.visible = True
        self.win = screen()
        self.color = colors()
        #self.height = win.height
        #self.width = win.width
        self.y = self.win.height - math.floor(self.win.height/6.0)
        
        # Ammo
        self.ammoX = math.floor(self.win.width/50)
        self.ammoY = self.win.height - math.floor(self.win.height/5.5)
        self.ammoC = self.color.white

        # Reload
        self.reloadX = math.floor(self.win.width/50)
        self.reloadY = self.win.height - math.floor(self.win.height/7)

        #Sets the image and scales it
        img = 'assets/hud/candy_cane.png'
        self.img = pygame.transform.rotate(pygame.image.load(img), -25)
        self.length, self.height = Image.open(img).size
        self.length, self.height = math.floor(self.length*4), math.floor(self.height*4)
        self.img = pygame.transform.scale(self.img, (self.length, self.height))

        self.grabs_msgs = ['Grabbing', 'Seizing', 'Grasping', 'Taking', 'Capturing', 'Snagging', 'Finding', 'Soul Searching', 'Detecting']
        self.grab_msg = random.choice(self.grabs_msgs) + ' Candy Canes'

    def update(self, win, player):
        if not player.reloading:
            self.drawAmmo(win, player)
        self.displayText(win, "SCORE: " + str(player.score), self.ammoX, self.win.height - self.win.height / 14, 32, self.color.white)

        

    def drawAmmo(self, win, player):
        #pygame.draw.rect(win, self.color, (self.mouseX, self.mouseY, self.length, self.height)) #creates reticle
        #pygame.draw.rect(win, self.color.black, (0, self.y, self.win.width, self.win.height)) #creates hud
        x, y = self.ammoX-25, 895
        for ammo in range(player.ammo):
            win.blit(self.img, (x, y))
            #pygame.draw.rect(win, self.color.white, (x, y, 10, 40))
            x += 40

    
    def displayText(self, win, text, x, y, fontSize, color):
        self.font = pygame.font.Font('freesansbold.ttf', fontSize)
        textDisplay = self.font.render(text , True, color)
        win.blit(textDisplay, (x, y))
    
    # Not currently used
    def swapColor(self, color):
        if color is self.color.white:
            return self.color.red
        elif color is self.color.red:
            return self.color.white
        else:
            print("color swapping error")
            return color

    def ammo(self, win, text, x, y, fontSize, reloading):
        if not reloading:
            self.ammoC = self.color.white
            self.displayText(win, text, x, y, fontSize, self.ammoC)
        else:
            self.reloading(win, self.grab_msg, self.reloadX, self.reloadY, 32, self.color.white)
            self.displayText(win, text, x, y, fontSize, self.ammoC)
    
    def reloading(self, win, text, x, y, fontSize, color):
        self.displayText(win, text, x, y, fontSize, color)

