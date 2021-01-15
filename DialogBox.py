from settings import *

class DialogBox(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 75))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, 250) 

        #INITIALIZE MESSAGING VARS
        self.msg_count = 0
        self.msgs = [
               "Testing 0...",
               "Testing 1...",
               "Testing 2...",
               "Testing 3...",
               "Testing 4...",
              ]
        self.NUM_MSGS = len(self.msgs)

        #CREATE TIMER TO DISPLAY MESSAGES
        self.msg_delay = 2500
        self.last_msg = pygame.time.get_ticks()
        
    def draw_text(self, surf, text, size, x, y, color):
        self.image.fill(PURPLE) #CLEAR ANY TEXT OFF THE SURFACE
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.image.blit(text_surface, text_rect)

    def get_next_message(self):
        return self.msgs[self.msg_count]

    def set_message_count(self, count):
        self.msg_count = count

    def update(self):

        #DISPLAY MESSAGES ONE AFTER THE OTHER
        now = pygame.time.get_ticks()
        if now - self.last_msg > self.msg_delay:
            self.last_msg = now

            self.draw_text(self.image,
                           self.get_next_message(),
                           22,
                           10,
                           10,
                           WHITE)
            self.msg_count += 1
            
            if self.msg_count > self.NUM_MSGS - 1:
                self.msg_count = 0
