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
