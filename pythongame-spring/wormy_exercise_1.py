import random, pygame, sys
from pygame.locals import *

FPS = 5
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

BGCOLOR     = (  0,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Wormy_exercise')
    runGame()

def runGame():
    startx = random.randint(7, CELLWIDTH - 6)
    starty = random.randint(7, CELLHEIGHT - 6)
    wormCoords = [[startx, starty], [startx-1, starty], 
        [startx-2, starty], [startx-3, starty], [startx-4, starty]]
    HEAD = 0
    direction = RIGHT

    while True: # main game loop
        for event in pygame.event.get(): 
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == K_RIGHT and direction != LEFT:
                    direction = RIGHT
                elif event.key == K_UP and direction != DOWN:
                    direction = UP
                elif event.key == K_DOWN and direction != UP:
                    direction = DOWN
                else:
                    break

                if direction == UP:
                    newHead = [wormCoords[HEAD][0], wormCoords[HEAD][1]-1]
                elif direction == DOWN:
                    newHead = [wormCoords[HEAD][0], wormCoords[HEAD][1]+1]
                elif direction == LEFT:
                    newHead = [wormCoords[HEAD][0]-1, wormCoords[HEAD][1]]
                elif direction == RIGHT:
                    newHead = [wormCoords[HEAD][0]+1, wormCoords[HEAD][1]]

                if newHead[0] >= 0 and newHead[0] < CELLWIDTH and \
                        newHead[1] >= 0 and newHead[1] < CELLHEIGHT:
                    wormCoords.insert(0, newHead)
                    del wormCoords[-1] 

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()

def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord[0] * CELLSIZE
        y = coord[1] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): 
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

if __name__ == '__main__':
    main()