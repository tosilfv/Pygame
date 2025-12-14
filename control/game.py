import pygame
from classes.screen import Screen
from classes.background import Background
from classes.player import Player

# Game
class Game:

    def __init__(self, screen, background, player) -> None:
        self.screen = screen
        self.background = background
        self.player = player

    def run(self):
        # Draw
        self.background.draw()
        self.player.draw()

        # Update
        pygame.display.update()
        self.player.update()

        # Clock
        game.screen.clock.tick(game.screen.framerate)

        # Print
        print(f'x: {game.player.rect_x}, y: {game.player.rect_y}')


# Create Objects
screen = Screen()
background = Background(screen)
player = Player(screen)

# Create Game
game = Game(screen, background, player)
