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



setDisplay = pygame.display.set_mode((400,300))
pygame.display.set_caption('Epic Game')

setDisplay.fill(cyan)

singlePixel = pygame.PixelArray(setDisplay)
singlePixel[3][3] = black

pygame.draw.line(setDisplay, blue, (389, 200), (300,70),4)


# main game loop
while True:
    for event in pygame.event.get():
        print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    