import pygame
import circleshape
from constants import LINE_WIDTH

class Asteroid(circleshape.CircleShape):
    def __init__ (self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        surface = screen
        color = "white"
        center = (self.x, self.y)
        pygame.draw.circle(screen, color, center, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.x = self.x + (self.velocity.x * dt)
        self.y = self.y + (self.velocity.y * dt)