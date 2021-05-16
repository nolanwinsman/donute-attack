from data import *

class playerObj(object):
    def __init__(self):
        self.score = 0
        self.color = colors().red
        self.mouseX = 0 # Default values
        self.mouseY = 0
        self.ammo = 6

    def update(self, win):
        self.draw(win)
        
    def draw(self, win):
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) #hides the mouse
        pygame.draw.rect(win, self.color, (self.mouseX, self.mouseY, 10, 10)) #creates reticle
    