import imp
import pygame
from settings import *
from utility import wave_value


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups,enemy_name):
        super().__init__(groups)

        self.image = pygame.Surface((TILE_SIZE//2,TILE_SIZE))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2

        #stats
        self.enemy_name = enemy_name
        self.enemy_stats = MONSTER_DATA[self.enemy_name]
        self.health = self.enemy_stats['health']

    def get_damage(self):
        pass
