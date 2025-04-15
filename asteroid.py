import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        #inherit circleshape
        CircleShape.__init__(self, x, y, radius)
        #store radius
        self.radius = radius
    
    def draw(self, screen):
        #overiding circleshape
        pygame.draw.circle(screen, "red", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        #overiding circleshape
        self.position += self.velocity * dt