from settings import *

#PLATFORM CLASS
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 25))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = HEIGHT - 80

    def update(self):
        self.rect.x += -5
        if self.rect.right < 0:
            self.rect.left = WIDTH
