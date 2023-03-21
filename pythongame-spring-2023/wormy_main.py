import pygame
from wormy_function import *

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Wormy")

    runGame_base(DISPLAYSURF, FPSCLOCK)

if __name__ == '__main__':
    main()