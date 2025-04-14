import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!") 
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
        #creating containers

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)
            #updating sprites.
        screen.fill((0, 0, 0))
            #setting screen color.
        for sprite in drawable:
            if isinstance(sprite, Player):
                sprite.draw(screen)
            elif isinstance(sprite, Asteroid):
                sprite.draw(screen)
            else:
                screen.blit(sprite.image, sprite.rect)
            #creating player sprite.
        
        dt = fps.tick(60) / 1000
            #setting framerate to 60fps.
            #print(f"DT: {dt}") #checking frame rate.
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
