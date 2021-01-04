from settings import *

class CrossHairs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(img_folder, "crosshairs.png")).convert()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

        self.pos = vec(0,0)
        self.timer = Timer()
        self.setCH = False

        self.old_x = 0
        self.old_y = 0
        
    def update(self):
        
        mouseState = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        
        self.pos.x = pos[0]
        self.pos.y = pos[1]

        if mouseState[0] == 1 and self.setCH == False:
            print("self.setCH", self.setCH)
            print("self.timer.start()", self.timer.start())
            
            self.old_x = pos[0]
            self.old_y = pos[1]

            self.setCH = True
            
        if self.setCH and self.timer.getElapsedTime() < 2:
            print("setting crosshairs") #set crosshairs for 2 secs
            self.rect.centerx = self.old_x
            self.rect.centery = self.old_y
        else:
            self.rect.centerx = self.pos.x
            self.rect.centery = self.pos.y
            self.setCH = False
