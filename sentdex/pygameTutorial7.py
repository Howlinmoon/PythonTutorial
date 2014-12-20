import pygame
import sys
from pygame.locals import *

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)



setDisplay = pygame.display.set_mode((300,300))
pygame.display.set_caption('Epic Game')

img = pygame.image.load('evilSquare.png')
imgx = 10
imgy = 10
pixMove = 1
FPS = 250
movement = "down"

fpsTime = pygame.time.Clock()


# main game loop
while True:
    setDisplay.fill(black)
    if movement == "down":
        imgy += pixMove
        if imgy > 200:
            img = pygame.transform.rotate(img,90)
            movement = 'right'
    
    elif movement == 'right':
        imgx += pixMove
        if imgx > 200:
            img = pygame.transform.rotate(img,90)
            movement = "up"
    
    elif movement == 'up':
        imgy -= pixMove
        if imgy < 30:
            img = pygame.transform.rotate(img,90)
            movement = 'left'
    
    elif movement == 'left':
        imgx -= pixMove
        if imgx < 30:
            img = pygame.transform.rotate(img,90)
            movement = 'down'
    
    
    setDisplay.blit(img, (imgx, imgy))
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fpsTime.tick(FPS)