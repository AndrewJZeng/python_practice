import pygame, sys, random
from pygame.locals import *

TILESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30

BGCOLOR =   (  0,   0,   0)
TILECOLOR = (  0, 204,   0)
NUM_ANAMATION = 8
SPEED = TILESIZE/NUM_ANAMATION

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Slide Animation')

    left = WINDOWWIDTH/2 - TILESIZE/2
    top = WINDOWHEIGHT/2 - TILESIZE/2

    while True: # main game loop
        DISPLAYSURF.fill(BGCOLOR)
        pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left, top, TILESIZE, TILESIZE))
        for event in pygame.event.get(): # get all the QUIT events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                # check if the user pressed a key to slide a tile
                if event.key == K_LEFT:
                    left, top = slideAnimation(left, top, -SPEED, 0)
                elif event.key == K_RIGHT:
                    left, top = slideAnimation(left, top, SPEED, 0)
                elif event.key == K_UP:
                    left, top = slideAnimation(left, top, 0, -SPEED)
                elif event.key == K_DOWN:
                    left, top = slideAnimation(left, top, 0, SPEED)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isValidMove(left, top):
    return left >=0 and left+TILESIZE <= WINDOWWIDTH \
            and top >= 0 and top+TILESIZE <= WINDOWHEIGHT

def slideAnimation(left, top, speedx, speedy):
    for i in range(NUM_ANAMATION):
        nextx = left + speedx
        nexty = top + speedy
        # animate the tile sliding over
        if isValidMove(nextx, nexty):
            DISPLAYSURF.fill(BGCOLOR)
            left, top = nextx, nexty
            pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left, top, TILESIZE, TILESIZE))
            pygame.display.update()
            FPSCLOCK.tick(FPS)    
        else:
            break
    return left, top

if __name__ == '__main__':
    main()

# generate 2-D array 
def generate_number_board(n):
    board = []
    counter = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(counter)
            counter += 1
        board.append(row)

    print(board)