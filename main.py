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

    screen.fill(BG_COLOR)
    level.run()
    pygame.display.update()
    clock.tick(60)

