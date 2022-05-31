from lib.cons import *

import pygame

def print_init_window(screen):
    # Fondo del nivel 1
    bg      =   pygame.image.load(BG1)
    bg_rect =   bg.get_rect()

    # Lo oscurecemos un poco con un fondo en alpha de la misma imagen superpuesto
    alpha   =   bg.convert_alpha()
    al_rect =   alpha.get_rect()
    alpha.fill(INIT_ALPHA)

    # Se añaden a la pantalla antes que el texto para que no lo esconda
    screen.blit(bg,bg_rect)
    screen.blit(alpha,al_rect)

    # Añadimos texto
    title_text  =   retro_font.render("SPACE INVADERS", True, WHITE)
    title_rect  =   title_text.get_rect(center=(WINDOW_WIDTH/2,100))

    


    # Imprimimos todos los textos
    screen.blit(title_text,title_rect)

