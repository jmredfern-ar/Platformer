# https://www.youtube.com/watch?v=fcryHcZE_sM&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=3

import pygame
import random
import os

WIDTH = 800
HEIGHT = 300
FPS = 30
GROUND = HEIGHT - 30

#CONSTANTS - PHYSICS
PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.9
vec = pygame.math.Vector2

#DEFINE COLORS
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

#PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.pos = vec(10, GROUND - 60)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):

        self.acc = vec(0, PLAYER_GRAV)    

        # CHECKS TO SEE WHICH KEYS WERE IN THE LIST (A.K.A. PRESSED)
        keystate = pygame.key.get_pressed() 
        if keystate[pygame.K_RIGHT]:
            self.acc.x += PLAYER_ACC
        if keystate[pygame.K_LEFT]:
            self.acc.x += -PLAYER_ACC
        if keystate[pygame.K_UP]:
            self.rect.y += -5
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
        if self.vel.y == 0 and keystate[pygame.K_SPACE]:
            self.vel.y = -20

        #APPLY FRICTION IN THE X DIRECTION
        self.acc.x += self.vel.x * PLAYER_FRICTION

        #EQUATIONS OF MOTION
        self.vel += self.acc                   #v = v0 + at
        self.pos += self.vel + 0.5 * self.acc  #s = s + v0t + 1/2at
        
        #WRAP AROUND THE SIDES OF THE SCREEN
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        #SIMULATE THE GROUND
        if self.pos.y > GROUND:
            self.pos.y = GROUND + 1
            self.vel.y = 0

        #SET THE NEW PLAYER POSITION BASED ON ABOVE
        self.rect.midbottom = self.pos
            
#PLATFORM CLASS
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 25))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = HEIGHT - 80

    def update(self):
        self.rect.x += -5
        if self.rect.right < 0:
            self.rect.left = WIDTH
        
#INITIALIZE VARIABLES
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

#ADD BACKGROUND
bkgr_image = pygame.image.load(os.path.join(img_folder, "background.jpg")).convert()
background = pygame.transform.scale(bkgr_image, (WIDTH, HEIGHT))
background_rect = background.get_rect()

#SPRITE GROUPS
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

platform = Platform()
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
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    # FLIP AFTER DRAWING
    pygame.display.flip()

pygame.quit()
