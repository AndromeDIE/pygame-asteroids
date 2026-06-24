from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def on_shot_hit(self):
        orig_velocity = self.velocity
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rotate_factor = 1
        for i in range(2):
            new_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid.velocity = orig_velocity.rotate(random.uniform(20, 50) * rotate_factor) * 1.2
            rotate_factor *= -1