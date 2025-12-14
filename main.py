import pygame
from sys import exit
from control.game import game

# Variables
running = True

# Game Loop
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    # Run
    game.run()

# Exit
pygame.quit()
exit()
