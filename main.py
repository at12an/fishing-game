from ast import main
from tkinter import RIGHT, LEFT, Canvas
from re import T
import pygame
from player import Fisher
from hook import Hook
import time
import random
from fish import Fish
from spritesheet import Spritesheet

pygame.init()


# Setup screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_info = pygame.display.Info()
pygame.display.set_caption('Fishing')
pygame.display.flip()
clock = pygame.time.Clock()

# Get screen info
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h

# Load Clouds
clouds = pygame.image.load('backgrounds/clouds.jpg')
clouds = pygame.transform.scale(clouds, (SCREEN_WIDTH, SCREEN_HEIGHT))
clouds_rect = clouds.get_rect()
clouds_rect.topleft = (0, 0)


# Load ocean
ocean = pygame.image.load('backgrounds/ocean2.PNG')
ocean = pygame.transform.scale(ocean, (SCREEN_WIDTH, 2*SCREEN_HEIGHT/3))
ocean_rect = ocean.get_rect()
ocean_rect.topleft = (0, SCREEN_HEIGHT/3)

# Initialise colours and background rects
sky_blue = (135, 206, 235)
sky_rect = (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT/3)

ocean_blue =  (0,94,184)
ocean_rect = (0, SCREEN_HEIGHT/3, SCREEN_WIDTH, 2*SCREEN_HEIGHT/3)

# Background drawers
def draw_sky():
    # screen.blit(clouds, clouds_rect)
    screen.fill(sky_blue, sky_rect)
    
def draw_water():
    # screen.blit(ocean, ocean_rect)
    screen.fill(ocean_blue, ocean_rect)
    
    
# Load Spritesheet
spritesheet = Spritesheet('images/spritesheet.png')
sprites = []
for i in range(1,14):
    sprites.append(pygame.transform.scale(spritesheet.parse_sprite('casting_' + str(i) + '.png'), (500, 500)))
sprite_count = 0
    
    
# Initialise fisherman
player = Fisher(SCREEN_WIDTH/2, SCREEN_HEIGHT/3)
hook = Hook(0,0,0,player)
print(SCREEN_WIDTH)
print(SCREEN_HEIGHT)


# Initialise fish
l = []


# Game state
score = 0
fishing_state = False


# Setup score
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)


# Game loop
run = True
while run:
    
    # Manage timescale
    clock.tick(60)
    
    
    
    # Draw background
    draw_sky()
    draw_water()
    
    # # Draw character
    # player.draw(screen)
    
    
    
    # Move character
    player.movement()
    
    # Events
    for event in pygame.event.get():
        # Quit Event
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            run = False
            
        # Key presses
        # Keyup
        if event.type == pygame.KEYDOWN:
            # X - start cast
            if event.key == pygame.K_x:
                start = time.time()
                fishing_state = False
        # Keydown     
        if event.type == pygame.KEYUP:
            # X - release cast
            if event.key == pygame.K_x:
                # Get cast speed
                sprite_count = 0
                fishing_state = True
                end = time.time()
                if (end - start < 5):
                    speed = 30 *(end - start)
                else:
                    speed = 15
                # Create hook object
                if (player.direction == LEFT):
                    hook = Hook(player.rect.left+120, player.rect.top, speed, player)
                else:
                    hook = Hook(player.rect.right+250, player.rect.top, speed, player)
                    
    keys = pygame.key.get_pressed()    
    # Run sprite animation
    if (keys[pygame.K_x]):
        if (player.direction == RIGHT):
            screen.blit(pygame.transform.flip(sprites[sprite_count % 8],True,False), (player.rect.x, player.rect.centery-125))
        else:  
            screen.blit(sprites[sprite_count % 8], (player.rect.x, player.rect.centery-125))
        if (sprite_count != 7):
            sprite_count += 1
    else:
        player.draw(screen)
           
           
                    
    # Print hook
    if fishing_state:
        hook.draw(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
        hook.sink(SCREEN_HEIGHT/3)
        hook.movement()
        
    spawn_fish = random.randrange(0,400)
    
    
    
    # Deal with fish
    if (spawn_fish == 55):
        fish_x = random.randrange(200, SCREEN_WIDTH - 200)
        fish_y = random.randrange(SCREEN_HEIGHT/2, SCREEN_HEIGHT - 200)
        fish = Fish(fish_x, fish_y)
        l.append(fish)
        
    fish_list = []
    for fishh in l:
        fishh.draw(screen)
        fishh.swim(SCREEN_HEIGHT/3, SCREEN_WIDTH)
        if (hook.rect.colliderect(fishh)):
            fish_list.append(fishh)
            
    for integer in fish_list:
        l.remove(integer)
        score += 1
    

    
    # Score
    text = font.render("Score: " + str(score), True, green, blue)
    textRect = text.get_rect()
    screen.blit(text, textRect)
    
    # Update window
    pygame.display.update()
    
pygame.quit()