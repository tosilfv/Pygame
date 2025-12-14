import pygame
from utils.constants.constants import CAPTION, FPS, SCREEN_HEIGHT, SCREEN_WIDTH

# Screen
class Screen():

    def __init__(self):
        self.scr = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.framerate = FPS
        pygame.display.set_caption(CAPTION)
