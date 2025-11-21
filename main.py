# Credits: Platformer Art Deluxe (Pixel) by Kenney Vleugels (www.kenney.nl)
# Music: Juhani Junkala

import pygame
import os
from sys import exit

# Run init before anything else
pygame.init()

# Setup Screen
scr_wid = 800
scr_hgt = 400
screen = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()
framerate = 60  # Times / second
test_font = pygame.font.Font("".join([os.path.dirname(__file__), "/font/Pixeltype.ttf"]), 50)

# Setup Surface
sur_wid = 100
sur_hgt = 200
sur_pos_origin = (0, 0)
sur_pos_ground = (0, 300)
sur_pos_text = (300, 200)
sky_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/sky.png"])).convert_alpha()
ground_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/ground.png"])).convert_alpha()
score_surface = test_font.render("00000", False, (64, 64, 64))
score_rect = score_surface.get_rect(center = (400, 50))
snail_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/snail/snail1.png"])).convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (900, 300))
player_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_walk_1.png"])).convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    # Check all possible types of inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
            # print('key pressed')
        if event.type == pygame.KEYUP:
            print('key released')

        # if event.type == pygame.MOUSEMOTION:
            # print(event.pos)
            # if player_rect.collidepoint(event.pos):
            #     print('collision')
    
    # Attach surfaces
    screen.blit(sky_surface, sur_pos_origin)
    screen.blit(ground_surface, sur_pos_ground)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 15)
    pygame.draw.line(screen, '#c0e8ec', (0,0), (800, 400), 15)
    pygame.draw.ellipse(screen, 'White', pygame.Rect(50, 200, 100, 100))
    screen.blit(score_surface, score_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    # if player_rect.colliderect(snail_rect):
    #     print("Collision!")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    # Draw all elements, update everything
    pygame.display.update()
    clock.tick(framerate)  # Do not run the while loop faster than framerate
