import pygame
import circleshape
import random 
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(circleshape.CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        surface = screen
        color = "white"
        center = self.position
        pygame.draw.circle(screen, color, center, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position.x = self.position.x + (self.velocity.x * dt)
        self.position.y = self.position.y + (self.velocity.y * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # log the split and generate a random angle
        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        # create two new asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        new_asteroid2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
        
        # set their velocities 
        new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
        new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
        