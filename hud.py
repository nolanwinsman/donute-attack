import pygame
from data import *
from player import *
import math


class hud:
    def __init__(self):
        self.visible = True
        self.win = screen()
        self.color = colors()
        #self.height = win.height
        #self.width = win.width
        self.y = self.win.height - math.floor(self.win.height/5.25)
        
        # Ammo
        self.ammoX = math.floor(self.win.width/20)
        self.ammoY = self.win.height - math.floor(self.win.height/5.5)
        self.ammoC = self.color.white

        # Reload
        self.reloadX = math.floor(self.win.width/20)
        self.reloadY = self.win.height - math.floor(self.win.height/7)
    
    def update(self, win):
        self.draw(win)
        

    def draw(self, win):
        #pygame.draw.rect(win, self.color, (self.mouseX, self.mouseY, self.length, self.height)) #creates reticle
        pygame.draw.rect(win, self.color.black, (0, self.y, self.win.width, self.win.height)) #creates hud
    
    def displayText(self, win, text, x, y, fontSize, color):
        self.font = pygame.font.Font('freesansbold.ttf', fontSize)
        textDisplay = self.font.render(text , True, color)
        win.blit(textDisplay, (x, y))
    
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
            #self.ammoC = self.swapColor(self.ammoC)
            self.reloading(win, "RELOADING", self.reloadX, self.reloadY, 32, self.color.white)
            self.displayText(win, text, x, y, fontSize, self.ammoC)
    
    def reloading(self, win, text, x, y, fontSize, color):
        self.displayText(win, text, x, y, fontSize, color)

