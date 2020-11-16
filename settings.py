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




