import pygame
from settings import *
from utility import import_folder


class AnimationPlayer:
    def __init__(self,groups) -> None:
        self.frames = {
            #dust particles
            'run': import_folder('img/character/dust_particles/run'),
            'land': import_folder('img/character/dust_particles/land'),
            'jump': import_folder('img/character/dust_particles/jump')
        }
        self.groups = groups

    def run_dust_particles(self,pos,direction_right:bool):
        if direction_right:
            animation_frames = self.frames['run']
        else:
            animation_frames = self.reflect_images(self.frames['run'])
            
        ParticleAnimations(self.groups,pos,animation_frames)
    
    def jump_dust_particles(self,pos):
        animation_frames = self.frames['jump']
        ParticleAnimations(self.groups,pos,animation_frames)

    def land_dust_particles(self,pos):
        animation_frames = self.frames['land']
        ParticleAnimations(self.groups,pos,animation_frames)
        

    def reflect_images(self,frames):
        new_frames = []

        for frame in frames:
            flip_frame = pygame.transform.flip(frame,True,False)
            new_frames.append(flip_frame)
        return new_frames


class ParticleAnimations(pygame.sprite.Sprite):
    def __init__(self,groups,pos,animation_frames) -> None:
        super().__init__(groups)

        self.frame_inx = 0
        self.animation_speed = 0.15
        self.animations = animation_frames
        self.image = self.animations[self.frame_inx]
        self.rect = self.image.get_rect(center = pos)


    def animate(self):
        self.frame_inx += self.animation_speed
        if self.frame_inx >= len(self.animations):
            self.kill()
        
        else:
            self.image = self.animations[int(self.frame_inx)]

    def update(self):
        self.animate()