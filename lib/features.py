from lib.cons import *
from lib.widgets import *

import pygame


class Init_Window():

    def __init__(self, screen, functions):
        self.screen = screen
        self.functions = functions

        # Fondo del nivel 1
        self.bg      =   pygame.image.load(BG1)
        self.bg_rect =   self.bg.get_rect()

        # Lo oscurecemos un poco con un fondo en alpha de la misma imagen superpuesto
        self.alpha   =   self.bg.convert_alpha()
        self.al_rect =   self.alpha.get_rect()
        self.alpha.fill(INIT_ALPHA)

        # Añadimos titulo
        self.title_text  =   retro_font_title.render("SPACE INVADERS", True, WHITE)
        self.title_rect  =   self.title_text.get_rect(center=(WINDOW_WIDTH/2,100))

        # Añadimos autor
        self.author_text =   retro_font.render("Author:", True, WHITE)
        self.name_text   =   retro_font.render("CoreDumbs", True, WHITE)
        self.author_rect =   self.author_text.get_rect(center=(WINDOW_WIDTH/2,480))
        self.name_rect   =   self.name_text.get_rect(center=(WINDOW_WIDTH/2,510))

        # Añadimos los otones de pantalla inicial
        self.btn_start       =   Button("START",     BTN_START_LOC,    retro_font_btn)
        self.btn_tutorial    =   Button("TUTORIAL",  BTN_TUTORIAL_LOC, retro_font_btn)
        self.btn_settings    =   Button("SETTINGS",  BTN_SETTINGS_LOC, retro_font_btn)
        self.btn_credits     =   Button("CREDITS",   BTN_CREDITS_LOC,  retro_font_btn)

    def draw(self): 
        # Se añaden a la pantalla antes que el texto para que no lo esconda
        self.screen.blit(self.bg,self.bg_rect)
        self.screen.blit(self.alpha,self.al_rect)

        # Imprimimos todos los textos
        self.screen.blit(self.title_text,self.title_rect)
        self.screen.blit(self.author_text,self.author_rect)
        self.screen.blit(self.name_text,self.name_rect)

        # Imprimimos los botones
        self.btn_start.draw(self.screen,self.functions['start'])
        self.btn_tutorial.draw(self.screen,self.functions['tutorial'])
        self.btn_settings.draw(self.screen,self.functions['settings'])
        self.btn_credits.draw(self.screen,self.functions['credits'])

class Play_Window():
    def __init__(self):
        pass

class Tutorial_Window():
    def __init__(self):
        pass

class Settings_Window():
    def __init__(self):
        pass

class Credits_Window():
    def __init__(self):
        pass