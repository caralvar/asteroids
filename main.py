import pygame
import sys


GAME_TITLE = "Asteroids"
MAIN_SCREEN_SIZE = (800, 800)
BACKGROUND_COLOR = "black"


pygame.init()
screen = pygame.display.set_mode(MAIN_SCREEN_SIZE)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    pygame.display.update()
    clock.tick(60)
