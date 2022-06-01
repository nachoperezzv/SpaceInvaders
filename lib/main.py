import pygame, sys

# -------------------
# Variables globales |
# -------------------
# Encargada de controlar la ventana en la que nos encontramos
# 0 -> pantalla de inicio: Jugar, Settings, Tutorial ...
# 1 -> pantalla de tutorial
# 2 -> pantalla de settings: Volumen música, Volumen efectos, ...
# 3 -> pantalla de credits
# 4 -> pantalla de juego
# Por poner: niveles
window      =   0


# -------------------
# Funciones botones  |
# -------------------
def start_fnc():
    global window
    window = 4

def tutorial_fnc():
    global window
    window = 1

def settings_fnc():
    global window
    window = 2

def credits_fnc():
    global window
    window = 3

def go_back():
    global window 
    window = 0

init_fncs   = {'start':start_fnc, 'tutorial':tutorial_fnc, 
                'settings':settings_fnc, 'credits':credits_fnc}

credit_fncs = {'go_back': go_back}

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

    init_window     = Init_Window(screen,init_fncs)
    credits_window  = Credits_Window(screen,credit_fncs)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #TODO: Añadir movimiento ligero al fondo para crear dinamismo
        if window == 0:
            init_window.draw()
        elif window == 1:
            pass
        elif window == 2:
            pass
        elif window == 3:
            credits_window.draw()
        elif window == 4:
            pass
            

        
        pygame.display.flip()


# Solo en caso de que se pretenda lanzar todo sin el main principal por comodidad
# El acceso a las librerias es diferente si se hace desde el main principal o desde el directorio
# lib. Por ello se importan las librerías en función de donde se compile el programa.
if __name__ == '__main__':
    from cons import *
    from features import *
    from widgets import *
    main()
else:
    from lib.cons import *
    from lib.features import *
    from lib.widgets import *