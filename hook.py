from tkinter import RIGHT, LEFT
import pygame
import math

class Hook():
    def __init__(self, x, y, speed, player):
        self.rect = pygame.Rect((x, y, 25, 25))
        self.rect.midright = (x,y)
        self.gravity = -speed
        self.player = player
        self.speed = speed
        self.direction = player.direction
        if (self.direction == LEFT):
            self.reel = (self.player.rect.left+130, self.player.rect.centery+35)
        else:
            
            self.reel = (self.player.rect.right+250, self.player.rect.centery+35)
        
    def calculate_distance(self, max):
        if (math.sqrt((self.rect.x-self.player.rect.x) ** 2 + (self.rect.y-self.player.rect.y) ** 2)) < max:
            return True
        return False
        
    def sink(self, sea_level):
        
        if (self.direction == LEFT):
            if (self.speed > 0):
                self.speed -= 1/5
        elif (self.direction == RIGHT):
            if (self.speed > 0):
                self.speed -= 1/5
            else:
                self.speed = 0
        if (self.rect.y > sea_level and self.gravity >= 0):
            self.gravity = self.gravity / 1.05
        elif (self.rect.y <= sea_level):
            self.gravity += 1
        if (self.calculate_distance(1600)):
            self.rect.y += self.gravity
            if (self.direction == LEFT):
                self.rect.x -= self.speed
            elif (self.direction == RIGHT):
                self.rect.x += self.speed
        
    def movement(self):
        keys = pygame.key.get_pressed()    
        if (keys[pygame.K_UP]):
            if (self.player.rect.left <= self.rect.right):
                self.rect.x -= 4
            elif (self.player.rect.right <= self.rect.left):
                self.rect.x += 4
            self.rect.y -= 4
        if (keys[pygame.K_DOWN]):
            self.rect.y += 2
        
    def draw(self, x, y, surface):
        hook_image = pygame.image.load('images/hook.png')
        hook_image = pygame.transform.scale(hook_image, (25, 45))
        if (self.direction == LEFT):
            hook_image = pygame.transform.flip(hook_image, True, False)
            pygame.draw.line(surface, (0,0,0), (self.player.rect.left+130, self.player.rect.top), self.rect.midtop)
        else:
            pygame.draw.line(surface, (0,0,0),(self.player.rect.right+250, self.player.rect.top), self.rect.midtop)
        surface.blit(hook_image, self.rect)
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)