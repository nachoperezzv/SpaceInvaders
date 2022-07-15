import pygame
import math

from cons import *

class Player(pygame.sprite.Sprite):
    def __init__(self):#'/../include/icons/spaceships/spaceship1.png'):
        super().__init__()

        self.s1     =   pygame.image.load(SHIP1).convert_alpha()
        self.s2     =   pygame.image.load(SHIP2).convert_alpha()
        self.s3     =   pygame.image.load(SHIP3).convert_alpha()
        self.s4     =   pygame.image.load(SHIP4).convert_alpha()
        self.s5     =   pygame.image.load(SHIP5).convert_alpha()
        self.s6     =   pygame.image.load(SHIP6).convert_alpha()
        self.s7     =   pygame.image.load(SHIP7).convert_alpha()
        self.s8     =   pygame.image.load(SHIP8).convert_alpha()
        self.s9     =   pygame.image.load(SHIP9).convert_alpha()
        self.spaceships  =   [self.s1,self.s2,self.s3,self.s4,self.s5,self.s6,self.s7,self.s8,self.s9]
        self.ship_index  =   0

        self.image = self.spaceships[self.ship_index]
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH/2,500))

    def player_input(self):
        self.keys = pygame.key.get_pressed()
        mx,my = pygame.mouse.get_pos()
        self.movement = 0
        
        booster = 1

        if self.keys[pygame.K_w]: 
            booster = 2
        if self.keys[pygame.K_q] and self.rect.x > -50:
            self.movement = -3 * booster
        if self.keys[pygame.K_e] and self.rect.x < 900:
            self.movement = 3 * booster 
        if self.keys[pygame.K_SPACE]:
            pass
        
        self.mouse_angle = int(math.degrees(math.atan2(self.rect.x-mx,self.rect.y-my)))

        self.image_rot = pygame.transform.rotate(self.image, self.mouse_angle)
        # self.rect_rot  = self.image.get_rect(center=(700,WINDOW_HEIGHT/2))
        self.image = self.image_rot
        

    
    def set_spaceship(self):
        self.ship_index = 4
        self.image = self.spaceships[self.ship_index]
        
    def move(self):
        self.rect.x += self.movement

    def update(self):
        self.set_spaceship()
        self.player_input()
        self.move()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = ''
        self.rect = ''
        self.mask = ''
    

    def update(self):
        pass


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = ''
        self.rect = ''
        self.mask = ''
    

    def update(self):
        pass