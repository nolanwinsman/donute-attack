import pygame
from PIL import Image
from data import screen
import math
import random

class pink_donut(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.screenData = screen()

        #Random coordinates for where they spawn
        self.x = random.randint(math.floor(self.screenData.width/100), self.screenData.width-math.floor(self.screenData.width/50))
        self.y = random.randint(math.floor(self.screenData.height/100), self.screenData.height-math.floor(self.screenData.height/4))
        
        #Sets the image and scales it
        self.length, self.height = Image.open(img).size
        self.length, self.height = self.length*6, self.height*6
        self.current_sprite = 0
        self.sprites = [pygame.transform.scale(pygame.image.load(img), (self.length, self.height))]
        self.animation_frames = 'defeated_pink/pink_Shot_Animated-'
        for i in range(1,8):
            frame = pygame.image.load(f'assets/donut/{self.animation_frames}{i}.png')
            self.sprites.append(pygame.transform.scale(frame, (self.length, self.height)))
        # the larger the number the faster the animation
        self.animation_speed = 0.1

        self.image = self.sprites[int(self.current_sprite)] # cast to int for animation_speed
        
        #Affects how fast the sprite moves
        self.deltaX = 1.5
        self.deltaY = -1.5 # TODO 1.5 and -1.5
        
        #Health
        self.health = 1
        self.alive = True
    
    def update(self, win):
        self.draw(win)
        self.image = self.sprites[int(self.current_sprite)]
        if self.health < 1:
            self.current_sprite += self.animation_speed
            if self.current_sprite >= len(self.sprites):
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
        win.blit(self.image, (self.x, self.y))

    def stop(self):
        if self.health < 1:
            self.deltaX = 0
            self.deltaY = 0


    def shot(self, win):
        self.stop()
        self.health -= 1

    # If the enemy is clicked
    def collidepoint(self, point):
        return pygame.Rect(self.x, self.y, self.length, self.height).collidepoint(point)

class red_donut(pink_donut):
    def __init__(self, img):
        super().__init__(img)


        self.sprites = [pygame.transform.scale(pygame.image.load(img), (self.length, self.height))]
        self.animation_frames = 'defeated_red/red_Shot_Animated-'

        for i in range(1,8):
            frame = pygame.image.load(f'assets/donut/{self.animation_frames}{i}.png')
            self.sprites.append(pygame.transform.scale(frame, (self.length, self.height)))

class blue_donut(pink_donut):
    def __init__(self, img):
        super().__init__(img)

        self.sprites = [pygame.transform.scale(pygame.image.load(img), (self.length, self.height))]
        self.animation_frames = 'defeated_blue/blue_Shot_Animated-'

        for i in range(1,8):
            frame = pygame.image.load(f'assets/donut/{self.animation_frames}{i}.png')
            self.sprites.append(pygame.transform.scale(frame, (self.length, self.height)))

        