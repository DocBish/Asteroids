import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        pygame.display.flip()
    print("Starting Asteroids!\n"
          f"Screen width: {SCREEN_WIDTH}\n"
          f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()