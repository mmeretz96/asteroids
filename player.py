from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame
import math

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.isShooting = False
        self.score = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def moveX(self, dt):
        self.position.x += dt*PLAYER_SPEED 

    def moveY(self, dt):
        self.position.y += dt*PLAYER_SPEED 

    def shoot(self, dt):
        if self.timer > 0: 
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.moveX(dt*(-1))
        if keys[pygame.K_d]:
            self.moveX(dt)
        if keys[pygame.K_w]:
            self.moveY(dt*(-1))
        if keys[pygame.K_s]:
            self.moveY(dt)

        if self.isShooting:
            self.shoot(dt)
                
        #Rotate player to mouse
        mouse_pos = pygame.mouse.get_pos()
        angle = math.degrees(math.atan2(mouse_pos[1] - self.position[1], mouse_pos[0] - self.position[0]))
        self.rotation = angle + 270

        self.timer -= dt