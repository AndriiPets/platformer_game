from os import walk
from math import sin
import pygame

def import_folder(path):
    surf_list = []

    for x,y,img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            load_img = pygame.image.load(full_path).convert_alpha()
            surf_list.append(load_img)
    return surf_list


def wave_value():
        val = sin(pygame.time.get_ticks())
        if val >= 0:
            return 255
        else:
            return 0
