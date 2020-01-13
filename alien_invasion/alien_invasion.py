import sys
import pygame
from settings import Settings
from ship import Ship
import time
def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        time.sleep(0.1)
        print(time.time())

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()

