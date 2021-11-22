import pygame
from pygame.locals import QUIT

def main():
    pygame.init()

    # set up the window
    displaysurf = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Drawing')

    draw_function(displaysurf)
    
    # run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        pygame.display.update()

def draw_function(displaysurf):
    black, white, red, green, blue = set_colors()

    displaysurf.fill(white)

    pygame.draw.polygon(displaysurf, green, ((146, 0), (291, 106),
                                             (236, 277), (56, 277), (0, 106)))
    pygame.draw.line(displaysurf, blue, (60, 60), (120, 60), 4)
    pygame.draw.line(displaysurf, blue, (120, 60), (60, 120))
    pygame.draw.line(displaysurf, blue, (60, 120), (120, 120), 4)
    pygame.draw.circle(displaysurf, blue, (300, 50), 20, 0)
    pygame.draw.ellipse(displaysurf, red, (300, 200, 40, 80), 1)
    pygame.draw.rect(displaysurf, red, (200, 150, 100, 50))

    draw_pixels(displaysurf, black)

def set_colors():
    black = (  0,   0,   0)
    white = (255, 255, 255)
    red   = (255,   0,   0)
    green = (  0, 255,   0)
    blue  = (  0,   0, 255)
    return [black, white, red, green, blue]

def draw_pixels(displaysurf, color):
    pixObj = pygame.PixelArray(displaysurf)
    pixObj[380][280] = color
    pixObj[382][282] = color
    pixObj[384][284] = color
    pixObj[386][286] = color
    pixObj[388][288] = color
    
if __name__ == '__main__':
    main()
