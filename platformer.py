
# https://www.youtube.com/watch?v=uWvb3QzA48c&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=18
import pygame
import random
import os

#CONSTANTS - GAME
WIDTH = 600
HEIGHT = 300
FPS = 30
GROUND = HEIGHT - 30

#CONSTANTS - PHYSICS
PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.9

#DEFINE COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ALEXYELLOW = (235, 194, 12)

#ASSET FOLDERS
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#PLAYER CLASS
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keystate = pygame.key.get_pressed()

        #ARROW KEY CONTROLS
        if keystate[pygame.K_UP]:
            self.rect.y += -5
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
        if keystate[pygame.K_LEFT]:
            self.rect.x += -5

        #WRAP AROUND THE SIDES OF THE SCREEN
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH

        #SIMULATE THE GROUND
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND -1
        
#PLATFORM CLASS
class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 25))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        #self.rect.center = (10, GROUND - 30)
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.x += -5
        if self.rect.right < 0:
            self.rect.left = WIDTH

#INITIALIZE VARIABLES
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()

#SPRITE GROUPS
all_sprites = pygame.sprite.Group()
player = Player(10, 10)
platform = Platform(10, GROUND - 60)
all_sprites.add(player)
all_sprites.add(platform)

# GAME LOOP:
#   Process Events
#   Update
#   Draw
running = True
while running:

    clock.tick(FPS)

    #PROCESS EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #UPDATE
    all_sprites.update()

    # DRAW
    screen.fill(ALEXYELLOW)
    all_sprites.draw(screen)

    # FLIP AFTER DRAWING
    pygame.display.flip()

pygame.quit()
