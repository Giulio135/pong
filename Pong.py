import pygame

class Player1(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load('player1.png'), (50,100))
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
        self.image = pygame.transform.scale(pygame.image.load('player1.png'), (50,100))
        self.x = DISPLAY_W - 30
        self.y = DISPLAY_H / 2
        self.rect = self.image.get_frect(center=(self.x, self.y))
        self.direction = pygame.math.Vector2()
        self.speed = 10
    def update(self):
        keys = pygame.key.get_pressed()
        self.direction.y =  int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.rect.center += self.direction * self.speed

DISPLAY_W = 500
DISPLAY_H = 500
running = True

all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

display_surf = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
player1 = Player1(all_sprites)
player2 = Player2(all_sprites)

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
