
from tkinter import LEFT, RIGHT
import time
import pygame
from hook import Hook

class Fisher():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 125, 250))
        self.rect.midbottom = (x,y-120)
        self.direction = LEFT
        self.image = pygame.image.load('images/casted_idle_state.png')
        self.image = pygame.transform.scale(self.image, (500, 500))
        
        
    def movement(self):
        keys = pygame.key.get_pressed()    
        if (keys[pygame.K_RIGHT]):
            if (self.direction == LEFT):
                self.image = pygame.transform.flip(self.image, True, False)
            self.direction = RIGHT
            self.rect.x += 8
        if (keys[pygame.K_LEFT]):
            if (self.direction == RIGHT):
                self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x -= 8
            self.direction = LEFT
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)
        
    def throw_hook(self):
        for event in pygame.event.get():
            start = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    start = time.time()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_x:
                    end = time.time()
                    if (end - start < 5):
                        speed = end - start
                    else:
                        speed = 5
                    self.hook = Hook(self.rect.left, self.rect.right, speed)
                        
                