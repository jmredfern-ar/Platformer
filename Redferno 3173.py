from settings import *
        
#INITIALIZE PYGAME
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

#ADD BACKGROUND
bkgr_image = pygame.image.load(os.path.join(img_folder, "background.jpg")).convert()
background = pygame.transform.scale(bkgr_image, (WIDTH, HEIGHT))
background_rect = background.get_rect()
bkgr_x = 0

#CREATE SPRITES, ADD TO GROUPS
'''
platform = Platform()
all_sprites.add(platform)
platforms.add(platform)
'''

player = Player()
all_sprites.add(player)

robot = Mob()
all_sprites.add(robot)

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
    rel_x = bkgr_x % background.get_rect().width
    screen.blit(background, (rel_x - background.get_rect().width, 0))
    if rel_x < WIDTH:
        screen.blit(background, (rel_x, 0))
    bkgr_x -= 1
    
    all_sprites.draw(screen)

    # FLIP AFTER DRAWING
    pygame.display.flip()

pygame.quit()
