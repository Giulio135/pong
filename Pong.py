import pygame

class Player1(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = 
        self.x = DISPLAY_W + 10
        self.y = DISPLAY_H / 2
        self.rect = self.image.get_frect(center=(self.x, self.y))
        self.direction = pygame.math.Vector2()
        self.speed = 10
    def update(self):
        pass

DISPLAY_W = 500
DISPLAY_H = 500
running = True

all_sprites = pygame.sprite.Group()

display_surf = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
player1 = Player1(all_sprites)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surf.fill('white')
    all_sprites.draw(display_surf)
    all_sprites.update()
    pygame.display.update()

pygame.quit()