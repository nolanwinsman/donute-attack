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
        self.width = 1920
        self.height = 1080

class pause:
    def __init__(self):
        self.paused = False
        self.backgroundColor = colors().yellow
        self.color = colors()

    def draw(self, win):
        pygame.draw.rect(win, self.color.red, (200, 200, 600, 100))
        self.displayText(win, "Null", 200, 200, 32, self.color.white)
      
    def displayText(self, win, text, x, y, fontSize, color):
        self.font = pygame.font.Font('freesansbold.ttf', fontSize)
        textDisplay = self.font.render(text , True, color)
        win.blit(textDisplay, (x, y))