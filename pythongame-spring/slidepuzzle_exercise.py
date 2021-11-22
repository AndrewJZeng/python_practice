import sys, pygame
from pygame.locals import *

def main(FPS=10):
    global BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Slide Puzzle Exercise')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    
    textColor = (0, 255, 0)
    textBGColor = (0, 0, 255)
    helloSurf, helloRect = makeText('Hello', textColor, textBGColor, 10, 10)
    worldSurf, worldRect = makeText('World', textColor, textBGColor, 50, 50)
    
    while True:
        DISPLAYSURF.fill((0,  0, 0))
        DISPLAYSURF.blit(helloSurf, helloRect)
        DISPLAYSURF.blit(worldSurf, worldRect)
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                # check if the user clicked on an option button
                if helloRect.collidepoint(event.pos):
                    textSurf, textRect = makeText('Hello is clicked', textColor, textBGColor, 100, 10)
                    DISPLAYSURF.blit(textSurf, textRect)
                elif worldRect.collidepoint(event.pos):
                    textSurf, textRect = makeText('World is clicked', textColor, textBGColor, 150, 50)
                    DISPLAYSURF.blit(textSurf, textRect)
        pygame.display.update()
        FPSCLOCK.tick(FPS)       

def makeText(text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text.
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1])) 
    else:
        main()
