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

# Setup Surface
sur_wid = 100
sur_hgt = 200
# sur_color = "Red"
sur_pos_origin = (0, 0)
# sur_pos_custom = (200, 100)
sky_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/Sky.png"]))
# sky_surface = pygame.Surface((sur_wid, sur_hgt))
# sky_surface.fill(sur_color)

while True:
    # Check all possible types of inputs
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Attach test surface
    screen.blit(sky_surface, sur_pos_origin)

    # Draw all elements
    # Update everything
    pygame.display.update()
    clock.tick(framerate)  # Do not run the while loop faster than framerate
