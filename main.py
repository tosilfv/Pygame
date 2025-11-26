# Credits: Platformer Art Deluxe (Pixel) by Kenney Vleugels (www.kenney.nl)
# Music: Juhani Junkala

import pygame
import os
from sys import exit
from random import randint, choice

########################
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_walk_1.png"])).convert_alpha()
        player_walk_2 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_walk_2.png"])).convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_jump.png"])).convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("".join([os.path.dirname(__file__), "/audio/jump.mp3"]))
        self.jump_sound.set_volume(0.1)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_frame_1 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/fly/fly1.png"])).convert_alpha()
            fly_frame_2 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/fly/fly2.png"])).convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210
        else:
            snail_frame_1 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/snail/snail1.png"])).convert_alpha()
            snail_frame_2 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/snail/snail2.png"])).convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill

########################

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f"Score: {current_time // 1000}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return (score_surf, score_rect, current_time // 1000)

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        # jump
        player_surface = player_jump
    else:
        # walk
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]
    # play walking animation if player is on floor
    # display jump surface if player jumps

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
# Game
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound("".join([os.path.dirname(__file__), "/audio/music.wav"]))
bg_music.set_volume(0.1)
bg_music.play(loops=-1)

########################
# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

########################

# Setup Surface
sur_wid = 100
sur_hgt = 200
sur_pos_origin = (0, 0)
sur_pos_ground = (0, 300)
sur_pos_text = (300, 200)
sky_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/sky.png"])).convert_alpha()
ground_surface = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/ground.png"])).convert_alpha()

# Obstacles
snail_frame_1 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/snail/snail1.png"])).convert_alpha()
snail_frame_2 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/snail/snail2.png"])).convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]
# snail_rect = snail_surface.get_rect(bottomright = (900, 300))

fly_frame_1 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/fly/fly1.png"])).convert_alpha()
fly_frame_2 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/fly/fly2.png"])).convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_walk_1.png"])).convert_alpha()
player_walk_2 = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_walk_2.png"])).convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_jump.png"])).convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load("".join([os.path.dirname(__file__), "/graphics/player/player_stand.png"])).convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))
text_title = test_font.render("Jumper Game", False, (64, 64, 64))
text_title_rect = text_title.get_rect(center = (400, 50))
text_instr = test_font.render("Press Space to Start", False, (64, 64, 64))
text_instr_rect = text_instr.get_rect(center = (400, 350))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    # Check all possible types of inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if player_rect.bottom == 300:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
                    # print('jump')
                # print('key pressed')
            # if event.type == pygame.KEYUP:
            #     print('key released')

            # if event.type == pygame.MOUSEMOTION:
            #     # print(event.pos)
            #     if player_rect.collidepoint(event.pos):
            #         print('collision')

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.bottom == 300:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    # snail_rect.left = 800
                    start_time = pygame.time.get_ticks()

        if game_active:
            if event.type == obstacle_timer:
                ########################
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
                ########################

                # if randint(0, 2):
                #     obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
                # else:
                #     obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

    if game_active:
        # Attach surfaces
        screen.blit(sky_surface, sur_pos_origin)
        screen.blit(ground_surface, sur_pos_ground)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 15)
        # pygame.draw.line(screen, '#c0e8ec', (0,0), (800, 400), 15)
        # pygame.draw.ellipse(screen, 'white', pygame.Rect(50, 200, 100, 100))
        # screen.blit(score_surface, score_rect)

        # snail_rect.x -= 4
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        # Player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # player_animation()
        # screen.blit(player_surface, player_rect)

        ########################
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Collision
        game_active = collision_sprite()
        ########################

        # Obstacle movement
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        # game_active = collisions(player_rect, obstacle_rect_list)

        # if player_rect.colliderect(snail_rect):
        #     game_active = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        # if player_rect.colliderect(snail_rect):
        #     print("Collision!")

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())
        score_surf, score_rect, score = display_score()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        if score > 0:
            screen.blit(score_surf, score_rect)
        else:
            screen.blit(text_title, text_title_rect)
            screen.blit(text_instr, text_instr_rect)


    # Draw all elements, update everything
    pygame.display.update()
    clock.tick(framerate)  # Do not run the while loop faster than framerate

print("Game Over.")
