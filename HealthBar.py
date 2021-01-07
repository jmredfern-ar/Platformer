from settings import *

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.healthbars = [
            pygame.image.load(os.path.join(img_folder, "health_bar0.png")).convert(),
            pygame.image.load(os.path.join(img_folder, "health_bar1.png")).convert(),
            pygame.image.load(os.path.join(img_folder, "health_bar2.png")).convert(),
            pygame.image.load(os.path.join(img_folder, "health_bar3.png")).convert(),
            pygame.image.load(os.path.join(img_folder, "health_bar4.png")).convert(),
            pygame.image.load(os.path.join(img_folder, "health_bar5.png")).convert()
            ]
        self.healthbar_count = 0

        self.image = self.healthbars[self.healthbar_count]
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.image.set_colorkey(BLACK)

        #ESTABLISH RECT, STARTING POINT
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

    def getHealth(self):
        return self.healthbar_count
    
    #PASS IN +1 OR -1 TO INCREMENT / DECREMENT HEALTH BAR
    def setHealth(self, health):
        if health == 1: #INCREASE HEALTH, UNLESS self.healthbar_count is at 0
            self.healthbar_count -= 1
            if self.healthbar_count < 0:
                self.healthbar_count = 0
        elif health == -1: #DECREASE HEALTH, UNLESS self.healthbar_count is at 5
            self.healthbar_count += 1
            if self.healthbar_count > 5:
                self.healthbar_count = 5

        
    def update(self):
        self.image = self.healthbars[self.healthbar_count]
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.image.set_colorkey(BLACK)
