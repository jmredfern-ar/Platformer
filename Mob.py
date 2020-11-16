from settings import *

#MOB CLASS
class Mob(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        print("Robot created...")
        #ADD ROBOT IMAGES
        self.robotRight = [
                            pygame.image.load(os.path.join(img_folder, "robotLeft0.png")).convert(),
                            pygame.image.load(os.path.join(img_folder, "robotLeft1.png")).convert(),
                            pygame.image.load(os.path.join(img_folder, "robotLeft2.png")).convert(),
                            pygame.image.load(os.path.join(img_folder, "robotLeft3.png")).convert(),
                            pygame.image.load(os.path.join(img_folder, "robotLeft4.png")).convert()
                          ]
        self.robot_count = 0
        self.image = self.robotRight[0]
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.image.set_colorkey(BLACK)

        #ESTABLISH RECT, POSITION                                     
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + 128
        self.rect.y = GROUND - 128
        self.speedx = -3

    def update(self):

        #TRANSITION BTW ROBOT IMAGES
        self.image = self.robotRight[self.robot_count]
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.image.set_colorkey(BLACK)

        self.robot_count += 1
        if self.robot_count > 4:
            self.robot_count = 0

        #CHANGE X POSITION
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.rect.left = WIDTH
            
