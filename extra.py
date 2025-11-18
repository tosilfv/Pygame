# Example


"""
# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()
"""




# Mediator Pattern


"""
class Mediator:
    def notify(self, sender, event):
        if event == "player_moved":
            print("Mediator: Player moved, notify enemies.")
            # Notify enemies to react to player movement

class Player:
    def __init__(self, mediator):
        self.mediator = mediator

    def move(self):
        print("Player: Moving.")
        self.mediator.notify(self, "player_moved")

class Enemy:
    def __init__(self, mediator):
        self.mediator = mediator

    def react_to_player(self):
        print("Enemy: Reacting to player movement.")

# Usage
mediator = Mediator()
player = Player(mediator)
enemy = Enemy(mediator)

player.move()  # Player moves and notifies the mediator
enemy.react_to_player()  # Enemy reacts based on mediator's notification
"""




# Manage State


"""
import pygame as pg
import sys

class States:
    def __init__(self):
        self.done = False
        self.next = None

class Menu(States):
    def __init__(self):
        super().__init__()
        self.next = 'game'

    def draw(self, screen):
        screen.fill((255, 0, 0))  # Red background for menu

class Game(States):
    def __init__(self):
        super().__init__()
        self.next = 'menu'

    def draw(self, screen):
        screen.fill((0, 0, 255))  # Blue background for game

class Control:
    def __init__(self):
        self.state_dict = {'menu': Menu(), 'game': Game()}
        self.state_name = 'menu'
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        self.state = self.state_dict[self.state.next]

    def main_game_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self.state.draw(pg.display.set_mode((600, 400)))
            pg.display.update()

app = Control()
app.main_game_loop()
"""
