import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        rotated_vel_1 = pygame.math.Vector2.rotate(self.velocity, angle)
        rotated_vel_2 = pygame.math.Vector2.rotate(self.velocity, -angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new_ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_rad)

        new_ast_1.velocity = rotated_vel_1 * 1.2
        new_ast_2.velocity = rotated_vel_2 * 1.2
