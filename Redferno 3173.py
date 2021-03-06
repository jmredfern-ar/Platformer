from settings import *

# CREATE SPRITES, ADD TO GROUPS
player = Player()
all_sprites.add(player)

healthBar = HealthBar()
all_sprites.add(healthBar)

shieldBar = ShieldBar()
all_sprites.add(shieldBar)

crossHairs = CrossHairs()
all_sprites.add(crossHairs)

dialogBox = DialogBox()  # Add to all_sprites dynamica lly

print(all_sprites)

timer = Timer()

# INITIALIZE CAMERA
'''
camera = Camera(background_rect.width, background_rect.height)
'''

newMob()
for i in range(NUM_PLATFORMS):
    newPlatform(i)

# GAME LOOP:
#   Process Events
#   Update
#   Draw
showing_dialog_box = False
start = True
end = False
cut_scene_1 = True
running = True
while running:

    # SHOW START SCREEN ONCE
    if start:
        show_start_screen()
        start = False

    if end:
        start = show_gameover_screen()
        end = False

    # SHOW CUT SCENE
    '''
    if cut_scene_1:
        show_cut_scene_1()
        cut_scene_1 = False
    '''
    clock.tick(FPS)

    # PROCESS EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                end = True

    player_orig_x = player.getPosX()

    # UPDATE SPRITES AND CAMERA
    all_sprites.update()
    '''
    camera.update(player)
    '''

    # CHECK TO SEE IF LASER HITS MOB
    #                                group1  group2   dokill1 dokill2
    hits = pygame.sprite.groupcollide(mobs, lasers, False, True)
    for hit in hits:
        hit.updateHealth(-1)
        # print(hit.getHealth())
        # newMob()

    # CHECK TO SEE IF MOB HITS PLAYER
    if player.getShieldOn() == False:
        hits = pygame.sprite.spritecollide(player, mobs, False)
        for hit in hits:
            robot_collision_sound.play()
            healthBar.setHealth(-1)
            # newMob()

    # PLAY HEALTH WARNING
    '''
    if healthBar.getHealth() == 5:
        healthbar_sound.play()
    '''

    # SCROLL THE BACKGROUND

    rel_x = bkgr_x % background.get_rect().width
    screen.blit(background, (rel_x - background.get_rect().width, 0))
    if rel_x < WIDTH:
        screen.blit(background, (rel_x, 0))
    bkgr_x -= 1

    # DRAW ALL THE SPRITES
    all_sprites.draw(screen)
    '''
    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))
    '''

    # FLIP AFTER DRAWING
    pygame.display.flip()

pygame.quit()
