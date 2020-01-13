import sys
import pygame
def run_game():
    pygame.init()
    screem = pygame.display.set_mode((900, 800))
    pygame.display.set_caption("Alien Invasion")
    bg = (255, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screem.fill(bg)
        pygame.display.flip()
run_game()

