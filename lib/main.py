import pygame, sys

# Función main para establecer la configuración de la pantalla, caption, icono, etc
def main():

    pygame.init()
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(pygame.image.load(ICON))
    
    main_loop()

# Creación de loop infinito mientras que no se cierre la aplicación o se decida 
# salir del juego
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


# Solo en caso de que se pretenda lanzar todo sin el main principal por comodidad
# El acceso a las librerias es diferente si se hace desde el main principal o desde el directorio
# lib. Por ello se importan las librerías en función de donde se compile el programa.
if __name__ == '__main__':
    from cons import *
    main()
else:
    from lib.cons import *