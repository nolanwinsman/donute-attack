import pygame
from data import *
import math


class hud:
    def __init__(self):
        self.visible = True
        self.win = screen()
        self.color = colors()
        #self.height = win.height
        #self.width = win.width
        self.y = self.win.height - math.floor(self.win.height/5.25)
        self.ammoX = math.floor(self.win.width/20)
        self.ammoY = self.win.height - math.floor(self.win.height/5.5)
    
    def update(self, win):
        self.draw(win)
        

    def draw(self, win):
        #pygame.draw.rect(win, self.color, (self.mouseX, self.mouseY, self.length, self.height)) #creates reticle
        pygame.draw.rect(win, self.color.black, (0, self.y, self.win.width, self.win.height)) #creates hud
    
    def displayText(self, win, text, x, y, fontSize):
        self.font = pygame.font.Font('freesansbold.ttf', fontSize)
        textDisplay = self.font.render(text , True, self.color.white)
        win.blit(textDisplay, (x, y))
