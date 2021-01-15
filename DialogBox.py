from settings import *

class DialogBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 75))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 250)
        
    def update(self):
        font_name = pygame.font.match_font('arial')
        #def draw_text(surf, text, size, x, y):
        size = 22
        text = "testing..."
        x = 10 #self.rect.centerx
        y = 10 #self.rect.centery
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.image.blit(text_surface, text_rect)
