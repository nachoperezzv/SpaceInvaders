import pygame, sys

# -------------------
# Variables globales |
# -------------------
# Encargada de controlar la ventana en la que nos encontramos
# 0 -> pantalla de inicio: Jugar, Settings, Tutorial ...
# 1 -> pantalla de tutorial
# 2 -> pantalla de configuración: Volumen música, Volumen efectos, ...
# Por poner: niveles
window      =   0

# Función main para establecer la configuración de la pantalla, caption, icono, etc
def main():

    pygame.init()
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(pygame.image.load(ICON))
    
    main_loop()

# Creación de loop infinito mientras que no se cierre la aplicación o se decida 
# salir del juego
def main_loop():
    global window

    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #TODO: Añadir movimiento ligero al fondo para crear dinamismo
        if window == 0:
            print_init_window(screen)
        else:
            pass
            

        
        pygame.display.flip()


# Solo en caso de que se pretenda lanzar todo sin el main principal por comodidad
# El acceso a las librerias es diferente si se hace desde el main principal o desde el directorio
# lib. Por ello se importan las librerías en función de donde se compile el programa.
if __name__ == '__main__':
    from cons import *
    from features import *
    main()
else:
    from lib.cons import *
    from lib.features import *