import pygame
import sys

import asteroid
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    astField = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        dt = clock.tick(60) / 1_000
        updatable.update(dt)
        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for stuff in shots:
                log_event("asteroid_shot")
                item.split()
                stuff.kill()

        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()
