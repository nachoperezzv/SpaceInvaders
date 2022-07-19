import pygame
import math
import random
import time

from cons import *

class Laser(pygame.sprite.Sprite):
    def __init__(self,start_pos,angle):
        super().__init__()
        
        self.theta = angle      # x angle
        self.phi = 90 - angle   # y angle

        self.speed_x = -8 * math.sin(math.radians(self.theta))
        self.speed_y = -8* math.sin(math.radians(self.phi))


        self.image = pygame.transform.rotate(pygame.Surface((1,15)),angle)
        self.image.fill('red')
        self.rect = self.image.get_rect(center=start_pos)
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def destroy(self):
        if self.rect.y < -10:
            self.kill()
    
    def update(self):
        self.move()
        self.destroy()


class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
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

        self.cooldown = 0.5
        self.cooling  = time.time()

        self.screen = screen
        self.laser = pygame.sprite.Group()
        
    def player_input(self):
        self.keys = pygame.key.get_pressed()
        mx,my = pygame.mouse.get_pos()
        self.movement = 0
        
        booster = 1

        if self.keys[pygame.K_w]: 
            booster = 2
        if self.keys[pygame.K_q]:
            self.movement = -3 * booster
        if self.keys[pygame.K_e]:
            self.movement = 3 * booster 
        
        self.mouse_angle = int(math.degrees(math.atan2(self.rect.x-mx,self.rect.y-my)))

        self.image_rot = pygame.transform.rotate(self.image, self.mouse_angle)
        self.image = self.image_rot

    def set_spaceship(self,spaceship):
        self.ship_index = spaceship
        self.image = self.spaceships[self.ship_index]
        
    def move(self):
        self.rect.x += self.movement

    def shoot(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and time.time() - self.cooling > self.cooldown:
            self.laser.add(Laser(self.rect.center,self.mouse_angle))
            self.cooling = time.time()
        
        self.laser.draw(self.screen)
        self.laser.update()

    def limits(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

    def update(self,spaceship):
        self.set_spaceship(spaceship)
        self.player_input()
        self.limits()
        self.shoot()
        self.move()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'asteroid1':
            self.asteroid = pygame.image.load(ASTEROID1).convert_alpha()
        elif type == 'asteroid2':
            self.asteroid = pygame.image.load(ASTEROID2).convert_alpha()
        elif type == 'asteroid3': 
            self.asteroid = pygame.image.load(ASTEROID3).convert_alpha()
        elif type == 'asteroid4':
            self.asteroid = pygame.image.load(ASTEROID4).convert_alpha()
        else:
            self.asteroid = pygame.image.load(ASTEROID5).convert_alpha()

        
        self.image  = self.asteroid
        self.rect   = self.image.get_rect(midbottom=(random.randint(50,850), -random.randint(100,150)))    

        self.direction = random.choice([1,0,0,-1])
        self.velocity  = random.choice([2,2.5,3])

    def asteroid_movement(self):        
        self.rect.x += self.direction
        self.rect.y += self.velocity

    def destroy(self):
        if self.rect.y > 700 or self.rect.x < -50 or self.rect.x > 950:
            self.kill()

    def update(self):
        self.asteroid_movement()
        self.destroy()


class Enemy(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'enemy1':
            self.enemy = pygame.image.load(ENEMY1).convert_alpha()
        elif type == 'enemy2':
            self.enemy = pygame.image.load(ENEMY2).convert_alpha()
        else: 
            self.enemy = pygame.image.load(ENEMY3).convert_alpha()
        
        
        self.image  = self.enemy
        self.rect   = self.image.get_rect(midbottom=(random.randint(50,850), -random.randint(100,150)))    

        self.direction = 0
        self.velocity  = random.choice([0.5,1,1.25])

    def enemy_movement(self):
        self.rect.x += self.direction
        self.rect.y += self.velocity
    
    def destroy(self):
        if self.rect.y > 650 or self.rect.x < -50 or self.rect.x > 950:
            self.kill()

    def update(self):
        self.enemy_movement()
        self.destroy()