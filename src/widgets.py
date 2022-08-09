from cons import *

import pygame

# class loc_params:
#     def __init__(self,left,top,width,height):
#         self.left   = left
#         self.top    = top
#         self.width  = width
#         self.height = height

class Button:
    def __init__(
                    self,text,btn_params,
                    font, elevation=3, 
                    text_color=[255,255,255],
                    btn_color_on=[195,195,195], btn_color_off=[175,175,175],
                    btn_color_bg=[25,25,25],
                    border_radius = 6
                ):

        #Core attributes 
        self.pressed            = False
        self.elevation          = elevation
        self.dynamic_elecation  = elevation
        self.pos                = [btn_params.left,btn_params.top]
        self.width              = btn_params.width
        self.height             = btn_params.height
        self.color_on           = btn_color_on
        self.color_off          = btn_color_off
        self.color_bg           = btn_color_bg
        self.border_radius      = border_radius
        # top rectangle 
        self.top_rect = pygame.Rect(self.pos,(self.width,self.height))
        self.top_color = self.color_off

        # bottom rectangle 
        self.bottom_rect = pygame.Rect(self.pos,(self.width,self.height))
        self.bottom_color = self.color_bg
        #text
        self.text_surf = font.render(text,True,text_color)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self, screen, function):
    # elevation logic 
        self.top_rect.y = self.pos[1] - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = self.border_radius)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = self.border_radius)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click(function)

    def check_click(self, function,kwargs=None):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.color_on
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    if kwargs == None:
                        function()
                    else:
                        function(**kwargs)
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = self.color_off
        
    def get_Rect(self):
        return self.top_rect


class Slider():
    def __init__(self, screen, params_bar, params_slider, index, font,
                bar_color = [255,255,255], slider_color = [225,225,225]):

        # Guardamos la pantalla
        self.screen         =   screen

        # Inicializamos fuentes
        self.font           =   font

        # Parametros para la barra (fija)
        self.left_bar       =   params_bar.left
        self.top_bar        =   params_bar.top
        self.width_bar      =   params_bar.width
        self.height_bar     =   params_bar.height

        # Parametros para el slider (movil)
        self.left_slide     =   params_slider.left
        self.top_slide      =   params_slider.top
        self.width_slide    =   params_slider.width
        self.height_slide   =   params_slider.height

        # Colores de la barra y el slider
        self.bar_color      =   bar_color
        self.slider_color   =   slider_color
        
        # Indíces: Valor inicial y final y la división que habrá entre un valor y otro
        self.first          =   index[0]
        self.last           =   index[1]
        self.div            =   index[2]

        # Marca en la que se encuentra el slider
        self.slider_mark    =   self.first

        # Creación de los rectángulos que formarán el slider 
        self.bar    =   pygame.Rect(self.left_bar,self.top_bar,
                                    self.width_bar,self.height_bar)

        self.slider =   pygame.Rect(self.left_slide,self.top_slide,
                                    self.width_slide,self.height_slide)

    def draw(self):   
                
        if pygame.mouse.get_pressed()[0]:
            mx,my = pygame.mouse.get_pos()

            if ( # se añade un +- 5 para que tenga holgura al clickar sobre una posición de la barra
                mx >= self.left_bar -50 and mx <= (self.left_bar + self.width_bar - self.width_slide + 50) and 
                my >= self.top_bar - 50  and my <= (self.top_bar  + self.height_bar) + 50
            ):
                # La nueva posición del top de bar vendrá dada por la posición mx
                # del mouse
                if mx > (self.left_bar + self.width_bar):
                    self.left_slide = self.left_bar + self.width_bar - self.width_slide
                elif mx < (self.left_bar):
                    self.left_slide = self.left_bar
                else:
                    self.left_slide = mx

                # Cambio en los parámetros del slider, la barra es fija             
                self.slider =   pygame.Rect(self.left_slide,self.top_slide,
                                    self.width_slide,self.height_slide)

        
        # Se dibujan la barra fija y movil del slider
        pygame.draw.rect(self.screen, self.bar_color, self.bar)
        pygame.draw.rect(self.screen, self.slider_color, self.slider)

        self.slider_mark    =   int((self.left_slide-self.left_bar)/(self.width_bar-self.width_slide) * (self.last) + self.first)
        self.slider_mark_txt=   str(self.slider_mark)

        mark_text   = self.font.render(str(self.slider_mark), True, [255,255,255])
        mark_rect   = mark_text.get_rect(center=(WINDOW_WIDTH/2,(self.top_bar + self.height_bar)+30))

        self.screen.blit(mark_text, mark_rect)

        return self.slider_mark


