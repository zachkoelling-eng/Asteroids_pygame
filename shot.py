import pygame
import circleshape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        surface = screen
        color = "white"
        center = self.position
        pygame.draw.circle(screen, color, center, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position.x = self.position.x + (self.velocity.x * dt)
        self.position.y = self.position.y + (self.velocity.y * dt)