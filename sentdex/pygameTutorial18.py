import random
import pygame
import sys
from pygame.locals import *

pygame.init()
fps = 30
dispWidth = 800
dispHeight = 600
cellSize = 10

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

bg = black


UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

deadZones = []

def whatNext():
    for event in pygame.event.get([KEYDOWN, KEYUP, QUIT]):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            continue
        return event.key
    return None

def makeTextObjs(text, font, tcolor):
    textSurface = font.render(text, True, tcolor)
    return textSurface, textSurface.get_rect()


def msgSurface(text, textColor):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)
    
    titleTextSurf, titleTextRect = makeTextObjs(text, largeText, textColor)
    titleTextRect.center = (int(dispWidth/2), int(dispHeight/2))
    setDisplay.blit(titleTextSurf,titleTextRect)
    
    typTextSurf, typTextRect = makeTextObjs('Press key to continue', smallText, white)
    typTextRect.center = (int(dispWidth/2), int(dispHeight/2)+120)
    setDisplay.blit(typTextSurf, typTextRect)
    fpsTime.tick()
    
    while whatNext() == None:
        for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        fpsTime.tick()
        
    runGame()
    
def evilMove(evilGuy):
    evilCoords = []
    # returns -1, 0, 1
    randomMovex = random.randrange(-1, 2)
    randomMovey = random.randrange(-1, 2)
    
    
    newCell = {'x':evilGuy[0]['x']+randomMovex, 'y':evilGuy[0]['y']+randomMovey}
    if (newCell['x'] < 0 or newCell['y'] < 0 or newCell['x'] > dispWidth/cellSize or newCell['y'] > dispHeight/cellSize):
        newCell = {'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}

    del evilGuy[-1]
    evilCoords.append(newCell['x'])
    evilCoords.append(newCell['y'])
    deadZones.append(evilCoords)
    
    evilGuy.insert(0, newCell)
    


def runGame():
    global deadZones
    startx = 3
    starty = 3
    coords = [{'x':startx, 'y':starty}]
    evilCoords1 = [{'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}]
    evilCoords2 = [{'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}]
    evilCoords3 = [{'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}]
    evilCoords4 = [{'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}]
    evilCoords5 = [{'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}]
    evilCoords6 = [{'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}]
    evilCoords7 = [{'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}]
    evilCoords8 = [{'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}]
    evilCoords9 = [{'x': dispWidth/(2 * cellSize), 'y': dispHeight/(2 * cellSize)}]
    
    direction = RIGHT
    isAlive = 'yes'
    
    while True:
        while isAlive == 'yes':
            deadZones = []
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
                
            if direction == UP:
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y'] - 1}
            
            elif direction == DOWN:
                newCell = {'x':coords[0]['x'], 'y':coords[0]['y'] + 1}
                
            elif direction == LEFT:
                newCell = {'x':coords[0]['x']-1, 'y':coords[0]['y']}
    
            elif direction == RIGHT:
                newCell = {'x':coords[0]['x']+1, 'y':coords[0]['y']}
    
            del coords[-1]
    
            coords.insert(0, newCell)
            setDisplay.fill(bg)
            
            evilMove(evilCoords1)
            evilMove(evilCoords2)
            evilMove(evilCoords3)
            evilMove(evilCoords4)
            evilMove(evilCoords5)
            evilMove(evilCoords6)
            evilMove(evilCoords7)
            evilMove(evilCoords8)
            evilMove(evilCoords9)
            
            
            drawCell(coords)
            drawCell(evilCoords1)
            drawCell(evilCoords2)
            drawCell(evilCoords3)
            drawCell(evilCoords4)
            drawCell(evilCoords5)
            drawCell(evilCoords6)
            drawCell(evilCoords7)
            drawCell(evilCoords8)
            drawCell(evilCoords9)
            
            currentPos = [newCell['x'], newCell['y']]
            
            for eachDeathCoord in deadZones:
                if eachDeathCoord == currentPos:
                    isAlive = 'no'
            
            pygame.display.update()
            fpsTime.tick(fps)
            
            if (newCell['x'] < 0 or newCell['y'] < 0 or newCell['x'] > dispWidth/cellSize or newCell['y'] > dispHeight/cellSize):
                isAlive = 'no'
                
        msgSurface('You Died!', red)
        
        
def drawCell (coords):
    for coord in coords:
        x = coord['x']*cellSize
        y = coord['y']*cellSize
        makeCell = pygame.Rect(x,y,cellSize, cellSize)
        pygame.draw.rect(setDisplay, blue, makeCell)

while True:
    global fpsTime
    global setDisplay
    
    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((dispWidth, dispHeight))
    pygame.display.set_caption('controlling')
    runGame()
    