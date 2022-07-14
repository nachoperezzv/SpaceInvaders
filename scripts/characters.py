import pygame

from lib.cons import *

class Player(pygame.sprite.Sprite):
    def __init__(self,default_ship = SHIP1):#'/../include/icons/spaceships/spaceship1.png'):
        super().__init__()

        self.image = pygame.image.load(default_ship).convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH/2,500))
        self.mask = ''
    

    def update(self):
        pass


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