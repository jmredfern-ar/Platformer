
import pygame as pg
import random
from os import path

image_dir = path.join(path.dirname(__file__), 'img')

TITLE = "BLADE RUNNER!"
WIDTH = 700
HEIGHT = 600
FPS = 60

# Player properties
PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.9

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40),
                 (125, HEIGHT - 350),
                 (500, 200),
                 (180, 50)]
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)                    
        self.game = game
        self.image = player_image
        #The cars size (Width, Height)
        self.image = pg.transform.scale(player_image, (160, 54))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(500, 170)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        #print("made a player")
        self.can_jump = True
        self.can_doublejump = True

    def jump(self):
        #jump only if standing on a platfrom
        self.rect.x =+ 1
        hits = pg.sprite.spritecollide(self,self.game.platforms, False)
        self.rect.x =+ 1
        '''
        if hits:
            self.vel.y = -20
        '''
        if self.can_jump and hits: #is standing on a platform
            self.can_jump = False
            self.vel.y = -25
            #print("jumping")
        elif self.can_doublejump:
            self.can_doublejump = False
            self.vel.y = -25
            #print("double jumping")

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH 
         # Load all game graphics


        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = random.choice(platform_images)
        print("image: ", self.image)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.goLeft = True

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        print("Making initial platforms...")
        self.run()
        

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        
        #check is player hits a platform- only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
                self.player.can_jump = True
                self.player.can_doublejump = True
                
        #if player reches top 1/4 of screen
        if self.player.rect.top <=HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    
        # spawn new platforms to keep same average number
        while len(self.platforms) < 5:
            print("num platforms: ", len(self.platforms))
            width = random.randrange(50, 100)
            buffer = 20
            if(self.goLeft):
                currentX = random.randrange(0, WIDTH / 2 - buffer)
                self.goLeft = False
                print("LEFT: ", currentX)
            else:
                currentX = random.randrange(WIDTH / 2 + buffer, WIDTH)
                self.goLeft = True
                print("RIGHT: ", currentX)
            p = Platform(currentX,
                         random.randrange(-100, -30))
            self.platforms.add(p)
            self.all_sprites.add(p)
                         
        
    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
                    

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.screen.blit(background, background_rect)
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass



g = Game()
g.show_start_screen()
platform_images = []
platform_list = ["andy.PNG","diego.PNG", "meg.PNG", "mikey.PNG","rene.PNG"]
for img in platform_list:
    platform_img =  pg.image.load(path.join(image_dir, img)).convert()
    image = pg.transform.scale(platform_img, (100, 50))
    platform_images.append(image)
temp_image = pg.image.load(path.join(image_dir, "back.PNG")).convert()
#background size
background = pg.transform.scale(temp_image, (WIDTH, HEIGHT))
background_rect = background.get_rect()
player_image = pg.image.load(path.join(image_dir, "car.png")).convert()


while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
