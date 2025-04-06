import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!") 
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    fps = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
            #setting screen color.
        player.draw(screen)
            #creating player sprite
        dt = fps.tick(60) / 1000
            #setting framerate to 60fps
            #print(f"DT: {dt}") #checking frame rate
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
