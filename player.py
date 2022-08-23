import pygame
from settings import *
from utility import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collisions:pygame.sprite.Group,bullet_attack) -> None:
        super().__init__(groups)

         #player grafix
        self.import_grafix()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        #player status
        self.status = 'idle'
        self.facing_right = True
        self.on_floor = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.current_x = 0

        #player movement
        self.direction = pygame.math.Vector2()
        self.speed = 6
        self.gravity_jump = 0.5
        self.gravity_fall = 0.9
        self.jump_height = 12
        self.collision_sprites = collisions
        

        #player attack 
        self.spawn_bullet = bullet_attack
        self.weapon_list = ['blaster','shotgun']
        self.weapon_type = self.weapon_list[0]
        self.weapon_inx = 0
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.weapon_switch_cooldown = 200

        #attack timer
        self.attack_ready = True
        self.attack_time = None
        self.attack_cooldown = 100

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_floor:
            self.direction.y = -self.jump_height

        if keys[pygame.K_z] and self.attack_ready:
            self.spawn_bullet(self.weapon_type)
            self.attack_ready = False
            self.attack_time = pygame.time.get_ticks()

        if keys[pygame.K_a] and self.can_switch_weapon:
            self.can_switch_weapon = False
            self.weapon_switch_time = pygame.time.get_ticks()
            
            if self.weapon_inx < len(self.weapon_list)-1:
                self.weapon_inx += 1
            else:
                self.weapon_inx = 0
            self.weapon_type = self.weapon_list[self.weapon_inx]
            print(self.weapon_type)


    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def import_grafix(self):
        char_path = 'img/character/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            path = char_path + animation
            self.animations[animation] = import_folder(path)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

        #set the rect
        if self.on_floor and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_floor and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_floor:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        


    def cooldown(self):
        curr_time = pygame.time.get_ticks()
        if not self.attack_ready:
            if curr_time - self.attack_time >= self.attack_cooldown:
                self.attack_ready = True

        if not self.can_switch_weapon:
            if curr_time - self.weapon_switch_time >= self.weapon_switch_cooldown:
                self.can_switch_weapon = True


    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                    self.on_left = True
                    self.current_x = self.rect.left
                elif self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                    self.on_right = True
                    self.current_x = self.rect.right

        if self.on_left and (self.rect.left < self.current_x or self.direction.x >= 0):
            self.on_left = False
        if self.on_right and (self.rect.right > self.current_x or self.direction.x <= 0):
            self.on_right = False
    
    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
                    self.on_ceiling = True
                elif self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
        
        if self.on_floor and self.direction.y < 0:
            self.on_floor = False
        if self.on_ceiling and self.direction.y > 0:
            self.on_ceiling = False

    def apply_gravity(self):
        if self.direction.y < 0:
            self.direction.y += self.gravity_jump
            self.rect.y += self.direction.y
        else: 
            self.direction.y += self.gravity_fall
            self.rect.y += self.direction.y


    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        self.cooldown()
        self.get_status()
        self.animate()