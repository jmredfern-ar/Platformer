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
        
    def update(self):
        
        mouseState = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
