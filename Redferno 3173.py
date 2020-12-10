from settings import *
        
#CREATE SPRITES, ADD TO GROUPS
player = Player()
all_sprites.add(player)

healthBar = HealthBar()
all_sprites.add(healthBar)

def newMob():
    robot = Mob()
    all_sprites.add(robot)
    mobs.add(robot)

newMob()

# GAME LOOP:
#   Process Events
#   Update
#   Draw
start = True
running = True
while running:

    #SHOW START SCREEN ONCE
    if start:
        show_start_screen()
        start = False

    clock.tick(FPS)

    #PROCESS EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_orig_x = player.getPosX()
 
    #UPDATE
    all_sprites.update()

    #CHECK TO SEE IF LASER HITS MOB
    ##                               group1  group2   dokill1 dokill2             
    hits = pygame.sprite.groupcollide(mobs,  lasers,   True,   True)
    for hit in hits:
        newMob()
    
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
