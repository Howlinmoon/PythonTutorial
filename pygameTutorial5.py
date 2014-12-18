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




# main game loop
while True:
    setDisplay.blit(img, (imgx, imgy))
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    