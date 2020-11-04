# https://www.youtube.com/watch?v=uWvb3QzA48c&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=18
import pygame
import random
import os

#CONSTANTS - GAME
WIDTH = 600
HEIGHT = 300
FPS = 30
GROUND = HEIGHT - 30
SLOW = 3
FAST = 8

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
ALEXYELLOW = (235, 194, 12)

#ASSET FOLDERS
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#DRAW TEXT
font_name = pygame.font.match_font("arial")
def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

#PLAYER CLASS
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, platforms):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        
        self.pos = vec(10, GROUND - 60)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.can_jump = True

    def update(self):

        self.acc = vec(0, PLAYER_GRAV)
        keystate = pygame.key.get_pressed()

        #ARROW KEY CONTROLS
        if keystate[pygame.K_UP]:
            self.rect.y += -5
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
        if keystate[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keystate[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if self.vel.y == 0 and keystate[pygame.K_SPACE]:
            self.vel.y = -20

        #APPLY FRICTION IN THE X DIRECTION
        self.acc.x += self.vel.x * PLAYER_FRICTION

        #EQUATIONS OF MOTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        #WRAP AROUND THE SIDES OF THE SCREEN
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        #SET THE NEW PLAYER POSITION BASED ON ABOVE
        self.rect.midbottom = self.pos

        #SIMULATE THE GROUND
        if self.pos.y > GROUND:
            self.pos.y = GROUND + 1
            self.vel.y = 0
  

        #HITS PLATFORM
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            if self.rect.top > hits[0].rect.top: #jumping from underneath
                self.pos.y = hits[0].rect.bottom + 25 + 1
                self.vel.y = 0
            else:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0

    def getStats(self):
        text = "Player\n" + "X: " + str(int(self.pos.x)) + ", Y: " + str(int(self.pos.y)) + "\n" + "ACC" + str(int(self.acc.x)) + " , " + str(int(self.acc.y))
        return text
        
#PLATFORM CLASS
class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, s):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 25))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = s
        
    def update(self):
        self.rect.x += -self.speed
        if self.rect.right < 0:
            #self.rect.left = WIDTH
            self.kill()
            
#GROUND CLASS
class Ground(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((600, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

#INITIALIZE VARIABLES
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()

#SPRITE GROUPS
#platform = Platform(10, GROUND - 60)
platforms = pygame.sprite.Group()
#platforms.add(platform)


ground = Ground(0, 270)
player = Player(10, 10, platforms)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
#all_sprites.add(platform)
all_sprites.add(ground)



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

    #SPAWN PLATFORMS
    while len(platforms) < 3:
        buffer = 20
        pX = random.randrange(WIDTH, WIDTH + 100)
        pY = random.randrange(30, GROUND - 60)
        pS = random.randrange(SLOW, FAST)
        print(pX, pY)
        p = Platform(pX, pY, pS)
        platforms.add(p)
        all_sprites.add(p)

    #UPDATE
    all_sprites.update()

    # DRAW
    screen.fill(ALEXYELLOW)
    draw_text(screen, "PLATFORMER", 24, 10, 10)
    text = player.getStats()
    draw_text(screen, text, 12, 10, 40)
    all_sprites.draw(screen)

    # FLIP AFTER DRAWING
    pygame.display.flip()

pygame.quit()

