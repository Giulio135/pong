import pygame
import random

class Player1(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.surface.Surface((20,100))
        self.image.fill((0,0,0))
        self.x = 30
        self.y = DISPLAY_H / 2
        self.rect = self.image.get_frect(center=(self.x, self.y))
        self.direction = pygame.math.Vector2()
        self.speed = 10
    def update(self):
        keys = pygame.key.get_pressed()
        self.direction.y =  int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.rect.center += self.direction * self.speed

class Player2(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.surface.Surface((20,100))
        self.image.fill((0,0,0))
        self.x = DISPLAY_W - 30
        self.y = DISPLAY_H / 2
        self.rect = self.image.get_frect(center=(self.x, self.y))
        self.direction = pygame.math.Vector2()
        self.speed = 10
    def update(self):
        keys = pygame.key.get_pressed()
        self.direction.y =  int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.rect.center += self.direction * self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.surface.Surface((20,20))
        self.image.fill((0,0,0))
        self.rect = self.image.get_frect(center=( DISPLAY_W / 2, DISPLAY_H / 2))
        self.direction = pygame.math.Vector2((random.uniform(-1,1),random.uniform(-1,1)))
        self.speed = 7
    def update(self):
        touching_sprite = pygame.sprite.groupcollide(balls, players, False, False)
        touching_edge = self.rect.y <= 0 or self.rect.y >= DISPLAY_H
        print(touching_edge)
        if touching_sprite:
            self.direction.x *= -1
        if touching_edge:
            self.direction.y *= -1
        self.direction = self.direction.normalize()
        self.rect.center += self.direction * self.speed

DISPLAY_W = 500
DISPLAY_H = 500
running = True

all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
balls = pygame.sprite.Group()

clock = pygame.time.Clock()

display_surf = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
player1 = Player1((all_sprites, players))
player2 = Player2((all_sprites, players))
ball = Ball((all_sprites, balls))

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surf.fill('white')
    all_sprites.draw(display_surf)
    all_sprites.update()
    pygame.display.update()

pygame.quit()
