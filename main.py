
import sys
import pygame
from settings import *
from level import Level

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('platformer')
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    level = Level(screen)
    

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                level.space_button = [True,False]
                #print('jump')
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                level.space_button = [False,True]
                #print('jump over')
        

    screen.fill(BG_COLOR)
    level.run()
    pygame.display.update()
    clock.tick(TARGET_FPS)

