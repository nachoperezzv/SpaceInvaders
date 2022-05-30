import pygame, sys

def main():

    pygame.init()
    pygame.display.set_caption(CAPTION)
    # pygame.image.load()
    
    main_loop()


def main_loop():
    
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill([0,0,0])

        cube = pygame.Rect(50,50,40,20)
        pygame.draw.rect(screen,[255,255,255],cube)

        pygame.display.flip()


if __name__ == '__main__':
    from cons import *
    main()

else:
    from lib.cons import *