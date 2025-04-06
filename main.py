import pygame
from constants import *

def main():
    print("Starting Asteroids!") 
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
fps = pygame.time.Clock()
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #setting screen color
    screen.fill((0, 0, 0))

    #setting framerate to 60fps
    dt = fps.tick(60) / 1000
    
    pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()
