from lib.widgets import *

import pygame

class Init_Window():

    def __init__(self, screen, functions):
        self.screen = screen
        self.functions = functions

        # Fondo predeterminado, que es el mismo que el del nivel 1
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


class Display_Selection():
    def __init__(self,screen):
        self.screen = screen

    def draw(self):
        pass


class Play_Window():
    def __init__(self,screen,fncs):

        self.screen     =   screen
        self.functions  =   fncs

        # Cambiamos el fondo
        # Fondo predeterminado, que es el mismo que el del nivel 1
        self.bg      =   pygame.image.load(BG1)
        self.bg_rect =   self.bg.get_rect()

        # Lo oscurecemos un poco con un fondo en alpha de la misma imagen superpuesto
        self.alpha   =   self.bg.convert_alpha()
        self.al_rect =   self.alpha.get_rect()
        self.alpha.fill(INIT_ALPHA)

        # Inicializamos las fuentes
        pygame.font.init()
        self.fonts = Fonts()

        # Titulo de PLAY e indicación de click donde sea para comenzar a jugar
        self.title_text =   self.fonts.retro_font_title.render("START PLAYING", True, WHITE)
        self.title_rect =   self.title_text.get_rect(center=(WINDOW_WIDTH/2,100))
        
        self.click_text =   self.fonts.retro_font.render("Click para empezar !!", True, WHITE)
        self.click_rect =   self.click_text.get_rect(center=(WINDOW_WIDTH/2,150))

        # Botón de vuelta atrás
        self.btn_back   =   Button("<-", BTN_GO_BACK, self.fonts.retro_font)

        # Botón de selección de nave
        self.btn_select =   Button("",BTN_SELECT_SPACESHIP, self.fonts.retro_font,border_radius=3)

        # Cuando pulsemos el botón de selección de nave espacial esta variable
        # pasará a tener valor True y nos mostrará todas las opciones posibles
        self.spaceship_selection = False

        # Inicialización de la pantalla de selección
        self.display_selection = Display_Selection(self.screen)

        # Esta variable guarda que nave usaremos para jugar.
        # Por defecto se juega con la número 1
        self.spaceship  =   1

    def draw(self):

        # Actualización del fondo para pasar de la pantalla inicial a la de creditos
        self.screen.blit(self.bg,self.bg_rect)
        self.screen.blit(self.alpha,self.al_rect)

        # Imprimimos el botón go back. Reestablece la variable window a valor = 0
        self.btn_back.draw(self.screen, self.functions['go_back'])

        # Printeamos los titulos e indicaciones
        self.screen.blit(self.title_text,self.title_rect)
        self.screen.blit(self.click_text,self.click_rect)

        if self.spaceship_selection == False:
            # Printeamos el botón de selección de personaje
            self.btn_select.draw(self.screen, self.spaceship_selection)
        
        else:
            # Printeamos pantalla de selección de nave
            # Cuando hayamos seleccionado una nos devolverá el número de nave elegida
            # y pondrá el valor de spaceship_selection a False de nuevo
            self.spaceship_selection, self.spaceship = self.display_selection_window()
    
    def select_spaceship(self):
        self.spaceship_selection = True
    
    def display_selection_window(self):
        self.display_selection.draw()
        


class Tutorial_Window():
    def __init__(self):
        pass

class Settings_Window():
    def __init__(self,screen,fncs):
    
        self.screen     =   screen
        self.functions  =   fncs

        # Cambiamos el fondo
        # Fondo predeterminado, que es el mismo que el del nivel 1
        self.bg      =   pygame.image.load(BG1)
        self.bg_rect =   self.bg.get_rect()

        # Lo oscurecemos un poco con un fondo en alpha de la misma imagen superpuesto
        self.alpha   =   self.bg.convert_alpha()
        self.al_rect =   self.alpha.get_rect()
        self.alpha.fill(INIT_ALPHA)

        # Inicializamos las fuentes
        pygame.font.init()
        self.fonts = Fonts()

        # Titulo de Settings 
        self.title_text =   self.fonts.retro_font_title.render("SETTINGS", True, WHITE)
        self.title_rect =   self.title_text.get_rect(center=(WINDOW_WIDTH/2,100))

        # Titulo de configuración sonido música
        self.music_text =   self.fonts.retro_font_btn.render("MÚSICA", True, WHITE)
        self.music_rect =   self.music_text.get_rect(center=(WINDOW_WIDTH/2,225))

        # Titulo de configuración sonido efectos
        self.effects_text   =   self.fonts.retro_font_btn.render("EFECTOS", True, WHITE)
        self.effects_rect   =   self.effects_text.get_rect(center=(WINDOW_WIDTH/2,425))

        # Creación de los sliders
        self.slider_music   =   Slider(self.screen,BAR_MUSIC, SLD_MUSIC, [0,100,1],self.fonts.retro_font) 
        self.slider_effects =   Slider(self.screen,BAR_EFFECTS, SLD_EFFECTS, [0,100,1],self.fonts.retro_font)

        # Botón de vuelta atrás
        self.btn_back    =   Button("<-", BTN_GO_BACK, retro_font)

    def draw(self):

        # Actualización del fondo para pasar de la pantalla inicial a la de creditos
        self.screen.blit(self.bg,self.bg_rect)
        self.screen.blit(self.alpha,self.al_rect)

        # Imprimimos el botón go back. Reestablece la variable window a valor = 0
        self.btn_back.draw(self.screen, self.functions['go_back'])
        
        # Printeamos titulo de settings y titulo de las posibles cosas a configurar
        self.screen.blit(self.title_text,self.title_rect)
        self.screen.blit(self.music_text,self.music_rect)
        self.screen.blit(self.effects_text,self.effects_rect)

        # Printeamos los sliders
        self.slider_music.draw()
        self.slider_effects.draw()


class Credits_Window():
    def __init__(self, screen, functions):
        self.screen     =   screen
        self.functions  =   functions

        # Inicializamos las fuentes en el fichero
        pygame.font.init()
        self.fonts      =   Fonts()

        # Actualizamos la pantalla a la de créditos
        # Fondo predeterminado, que es el mismo que el del nivel 1
        self.bg      =   pygame.image.load(BG1)
        self.bg_rect =   self.bg.get_rect()

        # Lo oscurecemos un poco con un fondo en alpha de la misma imagen superpuesto
        self.alpha   =   self.bg.convert_alpha()
        self.al_rect =   self.alpha.get_rect()
        self.alpha.fill(INIT_ALPHA)

        # Botón de vuelta atrás
        self.btn_back    =   Button("<-", BTN_GO_BACK, retro_font)

    def draw(self):

        # Actualización del fondo para pasar de la pantalla inicial a la de creditos
        self.screen.blit(self.bg,self.bg_rect)
        self.screen.blit(self.alpha,self.al_rect)

        # Imprimimos el botón go back. Reestablece la variable window a valor = 0
        self.btn_back.draw(self.screen, self.functions['go_back'])

        # Imprimimos los creditos
        self.print_credits()
    
    def print_credits(self):

        # Añadimos creditos de música
        self.music          =   self.fonts.retro_font.render("Music by:", True, WHITE)
        self.music_author   =   self.fonts.retro_font_btn.render("CoreDumbs", True, WHITE)

        self.music_rect     =   self.music.get_rect(center=(WINDOW_WIDTH/2,60))
        self.music_author_r =   self.music_author.get_rect(center=(WINDOW_WIDTH/2,120))

        self.screen.blit(self.music, self.music_rect)
        self.screen.blit(self.music_author, self.music_author_r)

        # Añadimos créditos de animación
        self.anim           =   self.fonts.retro_font.render("Animation by:", True, WHITE)
        self.anim_author    =   self.fonts.retro_font_btn.render("CoreDumbs", True, WHITE)

        self.anim_rect      =   self.anim.get_rect(center=(WINDOW_WIDTH/2,220))
        self.anim_author_r  =   self.anim_author.get_rect(center=(WINDOW_WIDTH/2,280))

        self.screen.blit(self.anim, self.anim_rect)
        self.screen.blit(self.anim_author, self.anim_author_r)

        # Añadimos autor
        self.author_text =   self.fonts.retro_font.render("Author:", True, WHITE)
        self.name_text   =   self.fonts.retro_font_btn.render("CoreDumbs", True, WHITE)
        
        self.author_rect =   self.author_text.get_rect(center=(WINDOW_WIDTH/2,380))
        self.name_rect   =   self.name_text.get_rect(center=(WINDOW_WIDTH/2,440))
        
        self.screen.blit(self.author_text, self.author_rect)
        self.screen.blit(self.name_text, self.name_rect)





