import pygame
from utils.constants.constants import ZERO

# Load Image
def load_image(path, default_color=(ZERO, 255, ZERO), default_size=(100, 100)):
    try:
        image = pygame.image.load(path).convert_alpha()
        return image
    except pygame.error as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: File not found in '{path}'")
    placeholder = pygame.Surface(default_size)
    placeholder.fill(default_color)
    return placeholder
