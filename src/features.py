from widgets import *
from characters import *

import pygame
import math

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
    def __init__(self,screen, fncs):
        
        # Guardamos la pantalla para tener una copia de ella y de las funciones
        self.screen     = screen
        self.functions  = fncs

        # Mantenemos fondo
        # Fondo predeterminado, que es el mismo que el del nivel 1
        self.bg      =   pygame.image.load(BG1)
        self.bg_rect =   self.bg.get_rect()

        # Lo oscurecemos un poco con un fondo en alpha de la misma imagen superpuesto
        self.alpha   =   self.bg.convert_alpha()
        self.al_rect =   self.alpha.get_rect()
        self.alpha.fill(INIT_ALPHA)

        # Inicializamos las fuentes
        self.fonts      =   Fonts()
       
        # Definición del borde que se utilizará para la pantalla de selección
        self.border      =  pygame.Rect(30,30,840,540) 

        # Creación del botón go_back de la pantalla de selección de la nave espacial
        # Botón de vuelta atrás
        self.btn_back   =   Button("<-", BTN_GO_BACK, self.fonts.retro_font)

        # Botones de selección de naves
        self.btn_s1     =   Button("", BTN_S1, self.fonts.retro_font,1,btn_color_off=LIGHT_GREY,btn_color_on=SOFT_LIGHT)
        self.btn_s2     =   Button("", BTN_S2, self.fonts.retro_font,1,btn_color_off=LIGHT_GREY,btn_color_on=SOFT_LIGHT)
        self.btn_s3     =   Button("", BTN_S3, self.fonts.retro_font,1,btn_color_off=LIGHT_GREY,btn_color_on=SOFT_LIGHT)
        self.btn_s4     =   Button("", BTN_S4, self.fonts.retro_font,1,btn_color_off=LIGHT_GREY,btn_color_on=SOFT_LIGHT)
        self.btn_s5     =   Button("", BTN_S5, self.fonts.retro_font,1,btn_color_off=LIGHT_GREY,btn_color_on=SOFT_LIGHT)
        self.btn_s6     =   Button("", BTN_S6, self.fonts.retro_font,1,btn_color_off=LIGHT_GREY,btn_color_on=SOFT_LIGHT)
        self.btn_s7     =   Button("", BTN_S7, self.fonts.retro_font,1,btn_color_off=LIGHT_GREY,btn_color_on=SOFT_LIGHT)
        self.btn_s8     =   Button("", BTN_S8, self.fonts.retro_font,1,btn_color_off=LIGHT_GREY,btn_color_on=SOFT_LIGHT)
        self.btn_s9     =   Button("", BTN_S9, self.fonts.retro_font,1,btn_color_off=LIGHT_GREY,btn_color_on=SOFT_LIGHT)

        # Definimos los botones para seleccionar una nave u otra
        self.s1         =   pygame.image.load(SHIP1)
        self.s1_rect    =   self.s1.get_rect(left=250,top=165)

        self.s2         =   pygame.image.load(SHIP2)
        self.s2_rect    =   self.s2.get_rect(left=425,top=150)

        self.s3         =   pygame.image.load(SHIP3)
        self.s3_rect    =   self.s3.get_rect(left=600,top=150)

        # ----

        self.s4         =   pygame.image.load(SHIP4)
        self.s4_rect    =   self.s4.get_rect(left=250,top=300)

        self.s5         =   pygame.image.load(SHIP5)
        self.s5_rect    =   self.s5.get_rect(left=425,top=300)

        self.s6         =   pygame.image.load(SHIP6)
        self.s6_rect    =   self.s6.get_rect(left=600,top=315)
        
        # ----
        
        self.s7         =   pygame.image.load(SHIP7)
        self.s7_rect    =   self.s7.get_rect(left=250,top=450)

        self.s8         =   pygame.image.load(SHIP8)
        self.s8_rect    =   self.s8.get_rect(left=425,top=450)

        self.s9         =   pygame.image.load(SHIP9)
        self.s9_rect    =   self.s9.get_rect(left=600,top=450)

        self.ships      =   [self.btn_s1, self.btn_s2, self.btn_s3,
                             self.btn_s4, self.btn_s5, self.btn_s6,
                             self.btn_s7, self.btn_s8, self.btn_s9]

        # Spaceship selected. Default = 1
        self.spaceship_selected = 0
    
    def select_S1(self): self.spaceship_selected = 1
    def select_S2(self): self.spaceship_selected = 2
    def select_S3(self): self.spaceship_selected = 3
    def select_S4(self): self.spaceship_selected = 4
    def select_S5(self): self.spaceship_selected = 5
    def select_S6(self): self.spaceship_selected = 6
    def select_S7(self): self.spaceship_selected = 7
    def select_S8(self): self.spaceship_selected = 8
    def select_S9(self): self.spaceship_selected = 9

    def draw(self):
        # Se printea otra vez el fondo para enmascarar los titulos de la anterior ventana
        self.screen.blit(self.bg,self.bg_rect)
        self.screen.blit(self.alpha,self.al_rect)

        self.ship_selected = 0

        # Dibujamos también un marco con color soft grey
        pygame.draw.rect(self.screen, LIGHT_GREY, self.border, width=5, border_radius=5)

        # Titulo de la ventana
        select_text =   self.fonts.retro_font_title.render("Elige tu nave espacial !",True,WHITE)
        select_rect =   select_text.get_rect(center=(WINDOW_WIDTH/2 - 10,70))
        self.screen.blit(select_text,select_rect)

        # Imprimimos los botones
        self.btn_back.draw(self.screen, self.functions['spaceship_selected_btn_go_back'])
        self.btn_s1.draw(self.screen, self.select_S1)
        self.btn_s2.draw(self.screen, self.select_S2)
        self.btn_s3.draw(self.screen, self.select_S3)
        self.btn_s4.draw(self.screen, self.select_S4)
        self.btn_s5.draw(self.screen, self.select_S5)
        self.btn_s6.draw(self.screen, self.select_S6)
        self.btn_s7.draw(self.screen, self.select_S7)
        self.btn_s8.draw(self.screen, self.select_S8)
        self.btn_s9.draw(self.screen, self.select_S9)

        # Rellenamos la superficie del botón de la nave que este seleccionada
        #self.ships[self.spaceship_selected].color_off = BLUE
        for i,s in enumerate(self.ships,1):
            if i == self.spaceship_selected:
                s.color_on  = [85,100,235]
                s.color_off = [64,64,255]
                self.ship_selected = i-1
            else:
                s.color_on  = [195,195,195]
                s.color_off = [175,175,175]

        # Las imagenes que van superpuestas a los botones
        self.screen.blit(self.s1,self.s1_rect)
        self.screen.blit(self.s2,self.s2_rect)
        self.screen.blit(self.s3,self.s3_rect)
        self.screen.blit(self.s4,self.s4_rect)
        self.screen.blit(self.s5,self.s5_rect)
        self.screen.blit(self.s6,self.s6_rect)
        self.screen.blit(self.s7,self.s7_rect)
        self.screen.blit(self.s8,self.s8_rect)
        self.screen.blit(self.s9,self.s9_rect)

        return self.ship_selected


class Play_Window():
    def __init__(self,screen,SS,fncs):

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
        
        self.click_text =   self.fonts.retro_font.render("Pulsa para empezar !!", True, WHITE)
        self.click_rect =   self.click_text.get_rect(center=(WINDOW_WIDTH/2,150))

        # Fin de juego
        self.icon       =   pygame.image.load(ICON2).convert_alpha()
        self.icon_rect  =   self.icon.get_rect(midbottom=(WINDOW_WIDTH/2,100))

        # Botón de vuelta atrás
        self.btn_back   =   Button("<-", BTN_GO_BACK, self.fonts.retro_font)

        # Botón de selección de nave
        self.btn_select =   Button("SPACESHIPS",BTN_SELECT_SPACESHIP, self.fonts.retro_font,border_radius=3)

        # Cuando pulsemos el botón de selección de nave espacial esta variable
        # pasará a tener valor True y nos mostrará todas las opciones posibles
        self.spaceship_selection = SS

        # Inicialización de la pantalla de selección
        self.display_selection = Display_Selection(self.screen, self.functions)

        # Esta variable guarda que nave usaremos para jugar.
        # Por defecto se juega con la número 1
        self.spaceship  =   0

        # Estado de la ventana:
        # SELECT_MODE      - selección ventana
        # LEVEL1           - nivel 1
        # LEVEL2           - nivel 2
        # LEVEL3           - nivel 3
        # END_OF_GAME      - juego ha finalizado
        self.state  =   SELECT_MODE

        # Puntuación total del juego
        self.score              =   0.00   
        self.asteroids_destroyed=   0
        self.enemies_destroyed  =   0
        self.final_score        =   0.00

        # Jugadores, enemigos y obstaculos
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(self.screen))

        self.obstacles = pygame.sprite.Group()

        self.enemies = pygame.sprite.Group()

    def selection(self, SS):
                
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.state = LEVEL1

        # SS es la variable del fichero main.py que es igual al valor 
        # de spaceship_selection

        # En función del estado de la variable se printea una cosa o la otra    
        self.spaceship_selection = SS

        if self.spaceship_selection == False:
            # Actualización del fondo para pasar de la pantalla inicial a la de juego
            self.screen.blit(self.bg,self.bg_rect)
            self.screen.blit(self.alpha,self.al_rect)

            # Imprimimos el botón go back. Reestablece la variable window a valor = 0
            self.btn_back.draw(self.screen, self.functions['go_back'])

            # Printeamos los titulos e indicaciones
            self.screen.blit(self.title_text,self.title_rect)
            self.screen.blit(self.click_text,self.click_rect)

            # Printeamos el botón de selección de personaje
            self.btn_select.draw(self.screen, self.functions['select_spaceship'])

        else:
            # Printeamos pantalla de selección de nave
            # Cuando hayamos seleccionado una nos devolverá el número de nave elegida
            # y pondrá el valor de spaceship_selection a False de nuevo
            self.spaceship = self.display_selection.draw()
    
    def display_score(self):
        self.score += 0.016

        score_text = self.fonts.retro_font.render('SCORE: {}'.format(int(self.score)), True, WHITE)
        score_rect = score_text.get_rect(topleft=(20,20))

        self.screen.blit(score_text,score_rect)

    def level(self,create_obstacle,create_enemy):

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.state = SELECT_MODE
        
        if create_obstacle:
            self.obstacles.add(Obstacle(random.choice(OBSTACLES)))
            self.obstacles.add(Obstacle(random.choice(OBSTACLES)))
        
        if create_enemy:
            self.enemies.add(Enemy(random.choice(ENEMIES)))
            pass

        self.screen.blit(self.bg,self.bg_rect)


        self.player.draw(self.screen)
        self.player.update(self.spaceship)

        self.obstacles.draw(self.screen)
        self.obstacles.update()

        self.enemies.draw(self.screen)
        self.enemies.update()

        self.display_score()

        if self.collision():
            self.state = END_OF_GAME

    def collision(self):

        if self.player.sprite.laser:
            for laser in self.player.sprite.laser:
                if bool(pygame.sprite.spritecollide(laser,self.obstacles,True)):
                    self.score += 5
                    self.asteroids_destroyed += 1
                    laser.kill()
                
                if bool(pygame.sprite.spritecollide(laser,self.enemies, True)):
                    self.score += 10
                    self.enemies_destroyed += 1
                    laser.kill()

        if (bool(pygame.sprite.spritecollide(self.player.sprite, self.obstacles, False)) == True or 
            bool(pygame.sprite.spritecollide(self.player.sprite, self.enemies, False)) == True):
            
            self.obstacles.empty()
            self.enemies.empty()

            self.final_score = self.score
            self.score = 0

            return True
        
        else: 
            return False

    def end_of_game(self):
        self.screen.blit(self.bg,self.bg_rect)
        self.screen.blit(self.alpha,self.al_rect)

        end_of_game_text = self.fonts.retro_font_title.render('Fin del juego !!', True, WHITE)
        end_score_text   = self.fonts.retro_font_btn.render('YOUR SCORE: {}'.format(int(self.final_score)), True, WHITE)
        statistic_text_1 = self.fonts.retro_font_btn.render('Asteroides destruidos: {}'.format(self.asteroids_destroyed), True, WHITE)
        statistic_text_2 = self.fonts.retro_font_btn.render('Enemigos abatidos: {}'.format(self.enemies_destroyed),True, WHITE)

        end_of_game_rect = end_of_game_text.get_rect(midtop=(WINDOW_WIDTH/2, 150))
        end_score_rect   = end_score_text.get_rect(midtop=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        statistic_rect_1 = statistic_text_1.get_rect(midtop=(WINDOW_WIDTH/2, 450))
        statistic_rect_2 = statistic_text_2.get_rect(midtop=(WINDOW_WIDTH/2, 500))

        self.screen.blit(end_of_game_text,end_of_game_rect)
        self.screen.blit(end_score_text,end_score_rect)
        self.screen.blit(statistic_text_1,statistic_rect_1)
        self.screen.blit(statistic_text_2,statistic_rect_2)

        self.screen.blit(self.icon,self.icon_rect)

    def draw(self,SS,create_obstacle,create_enemy):
        
        if self.state == SELECT_MODE: self.selection(SS)
        if self.state == LEVEL1:      self.level(create_obstacle,create_enemy)
        if self.state == END_OF_GAME: self.end_of_game()
        

class Tutorial_Window():
    def __init__(self,screen, fncs):
        
        # Guardamos la variable de la pantalla sobre la que dibujamos
        self.screen     = screen
        self.functions  = fncs

        # Inicializamos las fuentes
        pygame.font.init()
        self.fonts = Fonts()

        # Enunciados del tutorial
        self.tuto_text =   self.fonts.retro_font.render("Esto son los comandos que debes usar !!", True, WHITE)
        self.tuto_rect =   self.tuto_text.get_rect(center=(WINDOW_WIDTH/2,150))

        #TODO: Añadir botón E, su foto y su texto - BOOSTER
        self.qwe_text_1  =   self.fonts.retro_font_mini.render("Q:", True, WHITE)
        self.qwe_text_1_r=   self.qwe_text_1.get_rect(bottomleft=(110,350))
        self.qwe_text_2  =   self.fonts.retro_font_mini.render("Para moverse a la izquierda", True, WHITE)
        self.qwe_text_2_r=   self.qwe_text_2.get_rect(bottomleft=(130,350))
        self.qwe_text_3  =   self.fonts.retro_font_mini.render("W:", True, WHITE)
        self.qwe_text_3_r=   self.qwe_text_3.get_rect(bottomleft=(115,380))
        self.qwe_text_4  =   self.fonts.retro_font_mini.render("Para moverse más rápido", True, WHITE)
        self.qwe_text_4_r=   self.qwe_text_4.get_rect(bottomleft=(135,380))
        self.qwe_text_5  =   self.fonts.retro_font_mini.render("E:", True, WHITE)
        self.qwe_text_5_r=   self.qwe_text_5.get_rect(bottomleft=(112,410))
        self.qwe_text_6  =   self.fonts.retro_font_mini.render("Para moverse a la derecha", True, WHITE)
        self.qwe_text_6_r=   self.qwe_text_6.get_rect(bottomleft=(132,410))

        self.space_txt  =   self.fonts.retro_font_mini.render("Presione SPACE para disparar", True, WHITE)
        self.space_txt_r=   self.space_txt.get_rect(midbottom=(460,350))

        self.mouse_txt1 =   self.fonts.retro_font_mini.render("Posicione el ratón para", True, WHITE)
        self.mouse_txt1r=   self.mouse_txt1.get_rect(midbottom=(700,350))
        self.mouse_txt2 =   self.fonts.retro_font_mini.render("orientar el disparo", True, WHITE)
        self.mouse_txt2r=   self.mouse_txt2.get_rect(midbottom=(700,380))

        # Fondo predeterminado, que es el mismo que el del nivel 1
        self.bg      =   pygame.image.load(BG1)
        self.bg_rect =   self.bg.get_rect()

        # Imagenes de teclas que se van a usar
        self.qwe_key         =   pygame.image.load(QWE_KEY).convert_alpha()
        self.qwe_key_rect    =   self.qwe_key.get_rect(center=(210,WINDOW_HEIGHT/2))
        
        self.space_key      =   pygame.image.load(SPACE_KEY).convert_alpha()
        self.space_key_rect =   self.space_key.get_rect(center=(460, WINDOW_HEIGHT/2))
        
        self.mouse1         =   pygame.image.load(MOUSE1).convert_alpha()
        self.mouse2         =   pygame.image.load(MOUSE2).convert_alpha()
        self.mouses_img     =   [self.mouse1,self.mouse2]
        self.mouse          =   1
        self.mouse_rect     =   self.mouses_img[self.mouse].get_rect(center=(700,WINDOW_HEIGHT/2))

        self.mouse_angle    =   0

        
        # Lo oscurecemos un poco con un fondo en alpha de la misma imagen superpuesto
        self.alpha   =   self.bg.convert_alpha()
        self.al_rect =   self.alpha.get_rect()
        self.alpha.fill(INIT_ALPHA)

        # Botón de vuelta atrás
        self.btn_back   =   Button("<-", BTN_GO_BACK, self.fonts.retro_font)

        
    def draw(self):
        # Actualización del fondo para pasar de la pantalla inicial a la de juego
        self.screen.blit(self.bg,self.bg_rect)
        self.screen.blit(self.alpha,self.al_rect)

        # Se imprime el botón de vuelta atrás y los enunciados         
        self.btn_back.draw(self.screen, self.functions['go_back'])

        self.screen.blit(self.tuto_text,self.tuto_rect)

        self.screen.blit(self.qwe_text_1,self.qwe_text_1_r)
        self.screen.blit(self.qwe_text_2,self.qwe_text_2_r)
        self.screen.blit(self.qwe_text_3,self.qwe_text_3_r)
        self.screen.blit(self.qwe_text_4,self.qwe_text_4_r)
        self.screen.blit(self.qwe_text_5,self.qwe_text_5_r)
        self.screen.blit(self.qwe_text_6,self.qwe_text_6_r)

        self.screen.blit(self.space_txt,self.space_txt_r)

        self.screen.blit(self.mouse_txt1,self.mouse_txt1r)
        self.screen.blit(self.mouse_txt2,self.mouse_txt2r)
        
        # Imprimimos las imagenes y hacemos que el ratón gire
        self.screen.blit(self.qwe_key, self.qwe_key_rect)
        self.screen.blit(self.space_key, self.space_key_rect)

        mx, my = pygame.mouse.get_pos()

        if mx > 500 and mx < 800 and my > 150 and my < 450:
            self.mouse = 1
            self.mouse_angle = int(math.degrees(math.atan2(self.mouse_rect.x-mx,self.mouse_rect.y-my)))

            self.mouse_rot = pygame.transform.rotate(self.mouses_img[self.mouse], self.mouse_angle)
            self.mouse_rect = self.mouses_img[self.mouse].get_rect(center=(700,WINDOW_HEIGHT/2))

            self.screen.blit(self.mouse_rot, self.mouse_rect)

        else:
            self.mouse = 0
            self.mouse_rect = self.mouses_img[self.mouse].get_rect(center=(700,WINDOW_HEIGHT/2))
            self.screen.blit(self.mouses_img[self.mouse], self.mouse_rect)

        
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





