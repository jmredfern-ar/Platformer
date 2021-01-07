from settings import *

#PROJECTILE CLASS
class Laser(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, dest_x, dest_y):
        pygame.sprite.Sprite.__init__(self)

        #ADD LASER IMAGEs
    
        self.lasers = [
                       pygame.image.load(os.path.join(img_folder, "robotLaser" + "0.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "robotLaser" + "1.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "robotLaser" + "2.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "robotLaser" + "3.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "robotLaser" + "4.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "robotLaser" + "5.png")).convert()
                      ]
        
        self.laser_count = 0
        
        self.image = self.lasers[self.laser_count]
        self.image = pygame.transform.scale(self.image, (50, 10))
        self.image.set_colorkey(BLACK)

        #ESTABLISH RECT, STARTING POSITION
        self.rect = self.image.get_rect()
        self.rect.left = start_x
        self.rect.bottom = start_y

        #MAKE STARTING POINT MORE ACCURATE
        self.floating_point_x = start_x
        self.floating_point_y = start_y

        #DIFFERENCE BTW START AND DEST PTS
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        #APPLY VELOCITY
        self.speedx = 20
        self.change_x = math.cos(angle) * self.speedx
        self.change_y = math.sin(angle) * self.speedx

    def update(self):

        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        #TRANSITION BTW LASER PNGS
        self.image = self.lasers[self.laser_count]
        self.image = pygame.transform.scale(self.image, (50, 10))
        self.image.set_colorkey(BLACK)
        
        self.laser_count += 1
        if self.laser_count > 5:
            self.laser_count = 0

        #DELETE LASER ONCE OFF SCREEN
        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > WIDTH or self.rect.y < 0 or self.rect.y > HEIGHT:
            self.kill()
