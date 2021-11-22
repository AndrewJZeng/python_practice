import pygame, time
from pygame.locals import QUIT

delay = 0.01

def main():
    pygame.init()

    width, height = 320, 240
    speed = [1,1]
    black = (0, 0, 0)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Bouncing Ball')
    ball = pygame.image.load('intro_ball.gif')
    ballrect = ball.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.update()
        time.sleep(delay)

if __name__ == '__main__':
    main()

