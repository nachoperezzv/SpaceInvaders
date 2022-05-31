from lib.cons import *
import pygame

class loc_params:
    def __init__(self,left,top,width,height):
        self.left   = left
        self.top    = top
        self.width  = width
        self.height = height

class Button:
    def __init__(
                    self,text,btn_params,
                    font, elevation=3, 
                    text_color=[255,255,255],
                    btn_color_on=[195,195,195], btn_color_off=[175,175,175],
                    btn_color_bg=[25,25,25]
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

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 6)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 6)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click(function)

    def check_click(self, function):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.color_on
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    function()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = self.color_off
        
    def get_Rect(self):
        return self.top_rect