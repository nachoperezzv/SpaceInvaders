from lib.features import *

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

config_fncs = {'go_back': go_back}

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
    settings_window = Settings_Window(screen,config_fncs)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #TODO: Añadir movimiento ligero al fondo para crear dinamismo
        if window == 0:         # Init window
            init_window.draw()
        elif window == 1:       # Tutorial window
            pass
        elif window == 2:       # Settings window
            settings_window.draw()
        elif window == 3:       # Credits window
            credits_window.draw()
        elif window == 4:       # Play window
            pass
            

        
        pygame.display.flip()



    
