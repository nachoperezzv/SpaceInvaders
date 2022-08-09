from features import *

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

# Variable global para la selección de la nave
spaceship_selection_display = False

# Iniciando PYGAME
pygame.init()
clock = pygame.time.Clock()

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

def go_back_spaceship_selected():
    global spaceship_selection_display
    spaceship_selection_display = False 

def select_spaceship():
    global spaceship_selection_display
    spaceship_selection_display = True


init_fncs   = {'start':start_fnc, 'tutorial':tutorial_fnc, 
                'settings':settings_fnc, 'credits':credits_fnc}

credit_fncs = {'go_back': go_back}

config_fncs = {'go_back': go_back}

play_fncs   = {'go_back': go_back, 'select_spaceship': select_spaceship,
                'spaceship_selected_btn_go_back':go_back_spaceship_selected}

tutorial_fncs = {'go_back': go_back}

# Timers 
obstacle_timer = pygame.USEREVENT + 1
enemy_timer = pygame.USEREVENT + 2

pygame.time.set_timer(obstacle_timer, 2000)
pygame.time.set_timer(enemy_timer,5000)

# Función main para establecer la configuración de la pantalla, caption, icono, etc
def main():
    pygame.init()
    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(pygame.image.load(ICON))
    
    main_loop()

# Creación de loop infinito mientras que no se cierre la aplicación o se decida 
# salir del juego
def main_loop():
    global window, spaceship_selection_display
    global obstacle_timer, enemy_timer
    
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

    init_window     =   Init_Window(screen,init_fncs)
    play_window     =   Play_Window(screen,spaceship_selection_display,play_fncs)
    tutorial_window =   Tutorial_Window(screen, tutorial_fncs)
    credits_window  =   Credits_Window(screen,credit_fncs)
    settings_window =   Settings_Window(screen,config_fncs)

    music_volume = 1
    effects_volume = 1

    while True:

        create_obstacle = False
        create_enemy    = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == obstacle_timer:
                create_obstacle = True
            if event.type == enemy_timer:
                create_enemy = True

        if window == 0:         # Init window
            init_window.draw()

        elif window == 1:       # Tutorial window
            tutorial_window.draw()

        elif window == 2:       # Settings window
            music_volume, effects_volume = settings_window.draw()

        elif window == 3:       # Credits window
            credits_window.draw()

        elif window == 4:       # Play window
            play_window.draw(spaceship_selection_display ,create_obstacle, create_enemy, music_volume, effects_volume)       
                    
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()