import pygame
import sys
from pygame.locals import *
from distutils.command import upload

pygame.init()

white = (255,255,255)
black = (0,0,0)
bg = black

fps = 30
dispWidth = 800
dispHeight = 600
cellSize = 10

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

def runGame():
    startx = 3
    starty = 3
    coords = [{'x':startx, 'y':starty}]
    direction = RIGHT
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = LEFT
                    
                elif event.key == K_RIGHT:
                    direction = RIGHT
                
                elif event.key == K_UP:
                    direction = UP
                
                elif event.key == K_DOWN:
                    direction = DOWN
                
        