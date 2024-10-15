import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, center=self.position, radius=self.radius, width=2,color="white")
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            vector_one = self.velocity.rotate(rand_angle)
            vector_two = self.velocity.rotate(-rand_angle)
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = vector_one * ASTEROID_SPLIT_SPEED
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = vector_two * ASTEROID_SPLIT_SPEED