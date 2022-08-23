import pygame
from math import cos, sin,radians
from settings import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,groups,collisions:pygame.sprite.Group,direction_right:bool,attack_angle:int,player_pos,kill_distance:int):
        super().__init__(groups)
        
        self.image = pygame.Surface((TILE_SIZE//4,TILE_SIZE//4))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft = (x_pos,y_pos))
        self.collision_sprites = collisions
        self.start_pos = x_pos
        self.player_direction = direction_right
        self.player_pos = player_pos
        self.direction = pygame.math.Vector2(self.get_vec_coordinats(attack_angle))
        self.speed = 15
        self.distance = kill_distance

    def get_vec_coordinats(self,angle):
        rads = radians(angle)
        x = cos(rads)
        y = sin(rads)
        return (x,y)

    def move(self):
        bullet_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(self.player_pos)
        if self.player_direction:
            self.rect.x += self.direction.x * self.speed
            self.rect.y += self.direction.y * self.speed
            if (player_vec - bullet_vec).magnitude() >= self.distance:
                self.kill()
        else:
            self.rect.x -= self.direction.x * self.speed
            self.rect.y += self.direction.y * self.speed
            if (player_vec - bullet_vec).magnitude()  >= self.distance:
                self.kill()

    def check_collision(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.kill()



    def update(self):
        self.move()
        self.check_collision()