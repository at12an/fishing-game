import pygame
import random
import math

class Fish():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 150, 75))
        self.count = 0
        self.xmove = 0
        self.ymove = 0
        self.speed = 0
        self.image = pygame.image.load('images/fish2.png')
        
    def draw(self, surface):
        image = self.image
        image = pygame.transform.scale(image, (150, 75))
        surface.blit(image, self.rect)

    def swim(self, sea_level, right):
        if (self.count % 60 == 0):    
            self.speed = random.randint(0, 7)
            self.xmove = random.randint(-1, 1)
            self.ymove = random.randint(-1, 1)
        if (self.rect.left <= 0):
            self.xmove = 1
        if (self.rect.right >= right):
            self.xmove = -1
        if (self.rect.top <= sea_level):
            self.ymove = 1
        elif (self.rect.top >= sea_level*3):
            self.ymove = -1
        self.count += 1
        self.rect.x += self.xmove * self.speed
        self.rect.y += self.ymove * self.speed

    
    