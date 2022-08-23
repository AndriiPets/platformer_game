import pygame
from settings import *
from tile import Tile
from player import Player
from projectile import Projectile

class Level:
    def __init__(self,screen) -> None:
        
        #level setup
        self.display_surf = screen

        #sprite groups
        self.visible_sprites = CameraGroup(self.display_surf)
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.level_setup()

    def level_setup(self):
        for row_inx, row in enumerate(LEVEL_MAP):
            for col_inx, col in enumerate(row):
                x = col_inx * TILE_SIZE
                y = row_inx * TILE_SIZE

                if col == 'X':
                    Tile((x,y),[self.visible_sprites,self.collision_sprites])
                if col == 'P':
                    self.player = Player((x,y),[self.visible_sprites,self.active_sprites],
                    self.collision_sprites,
                    self.create_attack)

    def create_attack(self,weapon_type):
        if weapon_type == 'blaster':
            Projectile(self.player.rect.centerx,self.player.rect.centery,
            [self.visible_sprites,self.active_sprites],self.collision_sprites,self.player.facing_right,0,self.player.rect.center,700)
        if weapon_type == 'shotgun':
            Projectile(self.player.rect.centerx,self.player.rect.centery,
            [self.visible_sprites,self.active_sprites],self.collision_sprites,self.player.facing_right,0,self.player.rect.center,300),
            Projectile(self.player.rect.centerx,self.player.rect.centery,
            [self.visible_sprites,self.active_sprites],self.collision_sprites,self.player.facing_right,-18,self.player.rect.center,300),
            Projectile(self.player.rect.centerx,self.player.rect.centery,
            [self.visible_sprites,self.active_sprites],self.collision_sprites,self.player.facing_right,20,self.player.rect.center,300)


    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.active_sprites.update()


class CameraGroup(pygame.sprite.Group):
    def __init__(self,surface) -> None:
        super().__init__()
        self.display_surf = surface

        #camera setup
        cam_left = CAMERA_BORDERS['left']
        cam_top = CAMERA_BORDERS['top']
        cam_width = SCREEN_WIDTH - (cam_left + CAMERA_BORDERS['right'])
        cam_height = SCREEN_HEIGHT - (cam_top + CAMERA_BORDERS['bottom'])

        self.cam_rect = pygame.Rect(cam_left,cam_top,cam_width,cam_height)

    def custom_draw(self,player:Player):
        #set camera pos
        if player.rect.left < self.cam_rect.left:
            self.cam_rect.left = player.rect.left
        if player.rect.right > self.cam_rect.right:
            self.cam_rect.right = player.rect.right
        if player.rect.top < self.cam_rect.top:
            self.cam_rect.top = player.rect.top
        if player.rect.bottom > self.cam_rect.bottom:
            self.cam_rect.bottom = player.rect.bottom
        #camera offset
        self.offset = pygame.math.Vector2(
            self.cam_rect.left - CAMERA_BORDERS['left'],
            self.cam_rect.top - CAMERA_BORDERS['top']
        )
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surf.blit(sprite.image,offset_pos)
