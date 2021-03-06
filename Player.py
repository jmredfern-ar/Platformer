from settings import *

#PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #ADD PLAYER IMAGEs
        self.walkRight = [
                       pygame.image.load(os.path.join(img_folder, "walkright0.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "walkright1.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "walkright2.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "walkright3.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "walkright4.png")).convert()
                      ]

        self.shootRight = [
                       pygame.image.load(os.path.join(img_folder, "shootRight0.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "shootRight1.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "shootRight2.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "shootRight3.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "shootRight4.png")).convert()
                      ]

        self.shield = [
                       pygame.image.load(os.path.join(img_folder, "shield0.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "shield1.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "shield2.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "shield3.png")).convert(),
                       pygame.image.load(os.path.join(img_folder, "shield4.png")).convert()
                      ]
        self.player_count = 0
        self.image = self.walkRight[0]
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.image.set_colorkey(BLACK)

        #CREATE TIMER OBJ FOR VARIOUS USES
        #self.timer = Timer()

        #TRACK PLAYER DIRECTION
        self.actions = ["RIGHT", "LEFT", "UP", "DOWN", "SHOOTING", "JUMPING", "SHIELD", "NONE"]
        
        #ESTABLISH VECTORS FOR PHYSICS
        self.rect = self.image.get_rect()
        self.pos = vec(10, GROUND - 60)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        #SET UP SHOOTING
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

        #SET UP SHIELD
        self.shieldOn = False
        self.shieldCountDown = 0
        self.shieldCoolDown = 0

    def update(self):

        #INITIALIZE VARS
        self.action = "NONE"
        self.shieldOn = False
        self.canShoot = True
        self.acc = vec(0, PLAYER_GRAV)
        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_d]:
            self.action = "RIGHT"            
            self.acc.x += PLAYER_ACC
        if keystate[pygame.K_a]:
            self.action = "LEFT" 
            self.acc.x += -PLAYER_ACC
        if keystate[pygame.K_w]:
            self.action = "UP" 
            self.rect.y += -5
        if keystate[pygame.K_s]:
            self.action = "DOWN" 
            self.rect.y += 5
        if self.vel.y == 0 and keystate[pygame.K_SPACE]:
            self.action = "JUMPING"
            self.vel.y = -20
        if keystate[pygame.K_r]:
            pShield_sound.play()
            '''
            if shieldOn == False:
                start = time.time()
                stop = start + 3
                if time.time() < stop:
                    self.vel.x = 0
                    self.action = "SHIELD"
                    shieldOn = True
                else:
                    self.action = "NONE"
            '''
            self.action = "SHIELD"
                
        #CHECK FOR MOUSE EVENTS
        mouseState = pygame.mouse.get_pressed()
        if mouseState[0] == 1 and self.canShoot == True:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]

            self.action = "SHOOTING"
            shoot_sound.play()
            self.shoot(mouse_x, mouse_y)                   

        #APPLY FRICTION IN THE X DIRECTION
        self.acc.x += self.vel.x * PLAYER_FRICTION

        #TRANSITION BTW PLAYER PNGS
        if self.action == "RIGHT": #self.acc.x > 0 and self.vel.x > 0:
            self.image = self.walkRight[self.player_count]
            self.image = pygame.transform.scale(self.image, (128, 128))
            self.image.set_colorkey(BLACK)
            
            self.player_count += 1
            if self.player_count > 4:
                self.player_count = 0
                
        elif self.action == "SHOOTING":
            self.image = self.shootRight[self.player_count]
            self.image = pygame.transform.scale(self.image, (128, 128))
            self.image.set_colorkey(BLACK)
            
            self.player_count += 1
            if self.player_count > 4:
                self.player_count = 0
                
        elif self.action == "SHIELD":
            self.image = self.shield[self.player_count]
            self.image = pygame.transform.scale(self.image, (128, 128))
            self.image.set_colorkey(BLACK)

            self.player_count += 1
            if self.player_count > 4:
                self.player_count = 0
                    
        else:
            self.image = self.walkRight[0]
            self.image = pygame.transform.scale(self.image, (128, 128))
            self.image.set_colorkey(BLACK)
            
        #EQUATIONS OF MOTION
        self.vel += self.acc                   #v = v0 + at
        self.pos += self.vel + 0.5 * self.acc  #s = s + v0t + 1/2at
        
        #WRAP AROUND THE SIDES OF THE SCREEN
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        #SIMULATE THE GROUND
        if self.pos.y > GROUND:
            self.pos.y = GROUND + 1
            self.vel.y = 0

        #SET THE NEW PLAYER POSITION BASED ON ABOVE
        self.rect.midbottom = self.pos

    def shoot(self, mouse_x, mouse_y):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now

            laser = Laser(self.rect.right,    
                          self.rect.centery,
                          mouse_x,
                          mouse_y)
            
            all_sprites.add(laser)
            lasers.add(laser)

    def getPosX(self):
        return self.rect.x

    def getShieldOn(self):
        return self.shieldOn
