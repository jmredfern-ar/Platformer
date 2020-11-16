from settings import *

#PROJECTILE CLASS
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        #ADD LASER IMAGEs
        self.lasers = [
                       pygame.image.load(os.path.join(img_folder, "laser0.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "laser1.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "laser2.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "laser3.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "laser4.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "laser5.png")).convert()
                      ]
        self.laser_count = 0
        
        self.image = self.lasers[self.laser_count]
        self.image = pygame.transform.scale(self.image, (50, 10))
        self.image.set_colorkey(BLACK)

        #ESTABLISH RECT, STARTING POSITION
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.left = x
        self.speedx = 10

    def update(self):
        self.rect.x += self.speedx

        #TRANSITION BTW LASER PNGS
        self.image = self.lasers[self.laser_count]
        self.image = pygame.transform.scale(self.image, (50, 10))
        self.image.set_colorkey(BLACK)
        
        self.laser_count += 1
        if self.laser_count > 5:
            self.laser_count = 0

        #DELETE LASER ONCE OFF SCREEN
        if self.rect.left > WIDTH:
            self.kill()
