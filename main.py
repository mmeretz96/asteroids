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
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_over = False
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (drawable, asteroids, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()


         

    
    while True:
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    player.isShooting = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    player.isShooting = False

        if game_over:
            line_one = pygame.font.Font.render(my_font, f"GAME OVER ", False, "white")
            line_two = pygame.font.Font.render(my_font, f"Score: {player.score}", False, "white")
            line_three = pygame.font.Font.render(my_font, f"Press 'R' to respawn", False, "white")
            screen.fill("black")
            screen.blit(line_one, (50,SCREEN_HEIGHT/2 -50))
            screen.blit(line_two, (50,SCREEN_HEIGHT/2 -10))
            screen.blit(line_three, (50,SCREEN_HEIGHT/2 +30))
            pygame.display.flip()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_r]:
                game_over = False
                player.kill()
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                for asteroid in asteroids:
                    asteroid.kill()
            continue
        
        score_surface = pygame.font.Font.render(my_font, f"Score: {player.score}", False, "white")
        screen.fill("black")
        screen.blit(score_surface, (10,10))

        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if player.isColliding(asteroid):
                print("Game Over!")
                print(f"Player Score: {player.score}")
                game_over = True
            for shot in shots:
                if shot.isColliding(asteroid):
                    shot.kill()
                    player.score += 1
                    asteroid.split(dt)


        pygame.display.flip()

        


if __name__ == "__main__":
    main()