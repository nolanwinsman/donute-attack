from data import *
from PIL import Image

class playerObj(object):
    def __init__(self, img):
        self.score = 0
        self.c = colors()
        self.s = screen()
        self.mouseX = 0 # Default values
        self.mouseY = 0
        self.maxAmmo = 10
        self.ammo = self.maxAmmo
        # Reticle
        self.length = 10
        self.height = 10
        self.reloading = False
        self.reloadTime = 0
        self.img = pygame.image.load(img)
        self.reticleOffsetX = int(self.s.width/70) # offset is to center the reticle
        self.reticleOffsetY = int(self.s.height/40)
        self.imgLength, self.imgHeight = Image.open(img).size

    def update(self, win):
        self.draw(win)
        
    def draw(self, win):
        #win.blit(self.img, (self.mouseX - self.reticleOffsetX, self.mouseY - self.reticleOffsetY))
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) #hides the mouse
        # Creates reticle
        # TODO make this scale better with different resolutions
        pygame.draw.rect(win, self.c.red, (self.mouseX, self.mouseY, self.length, self.height))
        pygame.draw.rect(win, self.c.red, (self.mouseX+20, self.mouseY+3, 15, 4)) #reticle right
        pygame.draw.rect(win, self.c.red, (self.mouseX-25, self.mouseY+3, 15, 4)) #reticle left
        pygame.draw.rect(win, self.c.red, (self.mouseX+3, self.mouseY+20, 4, 15)) #reticle up
        pygame.draw.rect(win, self.c.red, (self.mouseX+3, self.mouseY-25, 4, 15)) #reticle down
        

    # When the player clicks
    def singleShot(self):
        # self.height, self.length = 11, 11
        self.ammo -= 1

        #self.img = pygame.transform.scale(self.img, (scaledLenght, scaledHeight))
    