'''
Credit to:
344276__nsstudios__laser3.wav
'''

#IMPORTS
import pygame
import random
import os

#CONSTANTS
WIDTH = 800
HEIGHT = 300
FPS = 30
GROUND = HEIGHT - 30
HW = WIDTH / 2
HH = HEIGHT / 2
AREA = WIDTH * HEIGHT

#CONSTANTS - PHYSICS
PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.9
vec = pygame.math.Vector2

#CONSTANTS - COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
JAREDBLUE = (154, 186, 237)
PURPLE = (255, 0, 255)

#ASSET FOLDERS
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
snd_folder = os.path.join(game_folder, "snd")

pygame.init()
pygame.mixer.init()

#LOAD SOUNDS
shoot_sound = pygame.mixer.Sound(os.path.join(snd_folder, "laser3.wav"))
pygame.mixer.music.load(os.path.join(snd_folder, "tgfcoder-FrozenJam-SeamlessLoop.ogg"))
pygame.mixer.music.set_volume(0.01)

#CREATE SPRITE GROUPS AND SPRITE OBJECTS
all_sprites = pygame.sprite.Group()
lasers      = pygame.sprite.Group()
platforms   = pygame.sprite.Group()
mobs        = pygame.sprite.Group()

#IMPORT USER-BUILT CLASSES
from Laser import Laser
from Player import Player
from Platform import Platform
from Mob import Mob
from HealthBar import HealthBar

#DRAW TEXT FUNCTION
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#INITIALIZE PYGAME
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Redferno 3173")

clock = pygame.time.Clock()
pygame.mixer.music.play(loops = -1) #continuous looping

#ADD BACKGROUND
bkgr_image = pygame.image.load(os.path.join(img_folder, "background.jpg")).convert()
background = pygame.transform.scale(bkgr_image, (WIDTH, HEIGHT))
background_rect = background.get_rect()
bkgr_x = 0

#SHOW START SCREEN FUNCTION
def show_start_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Redferno 3173!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Arrow keys to move, Space to jump, 'S' to fire", 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press a key to begin...", 18,  WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                print("Key pressed to start game!")
                waiting = False



