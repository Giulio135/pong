import pygame

DISPLAY_W = 500
DISPLAY_H = 500
running = True

all_sprites = pygame.sprite.Group()

display_surf = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surf.fill('white')
    pygame.display.update()

pygame.quit()
