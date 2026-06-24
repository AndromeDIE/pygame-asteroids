from constants import *
from circleshape import CircleShape
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0.0
    
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def move(self, dt: float) -> None:
        self.position += pygame.Vector2(0, 1).rotate(self.rotation) * dt * PLAYER_SPEED

    def rotate(self, dt: float) -> None:
        self.rotation += dt * PLAYER_TURN_SPEED
    
    def shoot(self, position, velocity) -> None:
        self.shot_cooldown_timer = 0.0
        shot = Shot(position.x, position.y)
        shot.velocity = velocity

    def update(self, dt: float) -> None:
        self.shot_cooldown_timer += dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE] and self.shot_cooldown_timer >= PLAYER_SHOOT_COOLDOWN:
            self.shoot(self.position, pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED)

