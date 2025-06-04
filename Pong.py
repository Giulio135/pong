import pygame
import random

pygame.init()

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
        self.image = pygame.surface.Surface((20, 20))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_frect(center=(DISPLAY_W / 2, DISPLAY_H / 2))
        self.direction = pygame.math.Vector2(random.choice([1, -1]), random.choice([-1, 1]))
        self.speed = 7
        self.resetting = False
        self.reset_start_time = 0

    def reset_position(self):
        self.rect.center = (DISPLAY_W / 2, DISPLAY_H / 2)
        self.direction = pygame.math.Vector2(random.choice([1, -1]), random.choice([-1, 1]))
        self.resetting = False

    def update(self):
        global points1, points2
        if self.resetting:
            now = pygame.time.get_ticks()
            if now - self.reset_start_time >= 2000:
                self.reset_position()
            return 
        touching_sprite = pygame.sprite.groupcollide(balls, players, False, False)
        touching_edge = self.rect.y <= 0 or self.rect.y >= DISPLAY_H
        if touching_sprite:
            self.direction.x *= -1
        if touching_edge:
            self.direction.y *= -1
        if self.rect.x <= 0:
            points2 += 1
            self.resetting = True
            self.reset_start_time = pygame.time.get_ticks()
        if self.rect.x >= DISPLAY_W:
            points1 += 1
            self.resetting = True
            self.reset_start_time = pygame.time.get_ticks()
        self.direction = self.direction.normalize()
        self.rect.center += self.direction * self.speed


DISPLAY_W = 500
DISPLAY_H = 500
running = True

all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
balls = pygame.sprite.Group()

clock = pygame.time.Clock()

points1 = 0
points2 = 0

font1 = pygame.font.Font(None, 50)

p1_win = font1.render('Jugador 1 ha ganado', True, (0,0,0))
p2_win = font1.render('Jugador 2 ha ganado', True, (0,0,0))

display_surf = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
player1 = Player1((all_sprites, players))
player2 = Player2((all_sprites, players))
ball = Ball((all_sprites, balls))

pause = False
while running:
    clock.tick(60)
    dt = pygame.time.get_ticks() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not pause:
        display_surf.fill('white')
        txt_p1 = font1.render(str(points1), True, (0,0,0))
        txt_p2 = font1.render(str(points2), True, (0,0,0))
        display_surf.blit(txt_p1, (20,20))
        display_surf.blit(txt_p2, (DISPLAY_W-20,20))
        all_sprites.draw(display_surf)
        all_sprites.update()
        pygame.display.update()

    if points1 >= 5:
        display_surf.blit(p1_win, (80,100))
        pygame.display.update()
        pause = True
    if points2 >= 5:
        display_surf.blit(p2_win, (80,100))
        pygame.display.update()
        pause = True

pygame.quit()
