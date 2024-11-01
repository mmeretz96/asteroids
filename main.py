import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (drawable, asteroids, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if player.isColliding(asteroid):
                print("Game Over!")
                return 
            for shot in shots:
                if shot.isColliding(asteroid):
                    shot.kill()
                    asteroid.split(dt)


        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()