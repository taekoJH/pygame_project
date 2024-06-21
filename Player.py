import pygame
from pygame.locals import *
from HealthBar import HealthBar
from Fireball import Fireball
import ipdb

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Images/Player_Sprite_R.png")
        self.rect = pygame.Rect(x, y, 35, 50)

        self.pos = vec(x, y) #try
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)
        self.healthBar = HealthBar(10, 10)
        self.mana = 50
        self.maxMana = 100
        self.coins = 20
        self.manaPotions = 3

        self.ACC = 0.4
        self.FRIC = -0.1


        self.jumping = False
        self.running = False
        self.direction = "RIGHT"
        self.move_frame = 0


        self.attacking = False
        self.attack_frame = 0
        self.attack_counter = 0

        #############################################################
        ####################### PHASE 2 #############################
        #############################################################
        # Dash parameter
        self.dashing = False
        self.dash_frame = 0
        self.dash_counter = 0

        # Defend parameter
        self.defending = False
        self.defend_frame = 0
        self.defend_counter = 0

        #############################################################
        ####################### PHASE 2 #############################
        #############################################################

        self.attack_range = pygame.Rect(0, 0, 0, 0)
        self.hit_cooldown = False


        # Player Events
        self.hit_cooldown_event = pygame.USEREVENT + 1


    def move(self):

        self.acc = vec(0, 0.5)

        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.acc.x = -self.ACC
        if keys[K_RIGHT]:
            self.acc.x = self.ACC

        #############################################################
        ####################### PHASE 2 #############################
        #############################################################
        if self.dashing:
            if self.direction == "RIGHT":
                self.vel.x = 10     # dash
            elif self.direction == "LEFT":
                self.vel.x = -10    # dash
        #############################################################
        ####################### PHASE 2 #############################
        #############################################################

        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > 800:
            self.pos.x = 0
        elif self.pos.x < -30:
            self.pos.x = 800
        
        self.rect.topleft = self.pos
        self.rect.x += 32

    def walking(self):
        if self.move_frame > 6:
            self.move_frame = 0
            return

        if self.jumping == False and self.running == True:
            if self.vel.x >= 0:
                self.image = self.animation_right[self.move_frame]
                self.direction = "RIGHT"
            elif self.vel.x < 0:
                self.image = self.animation_left[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1

        if self.running == False and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = self.animation_right[self.move_frame]
            elif self.direction == "LEFT":
                self.image = self.animation_left[self.move_frame]

    def attack(self):
        if self.attacking == True:
            if self.direction == "RIGHT":
                self.attack_range = pygame.Rect(self.rect.x + self.rect.width,self.pos.y, 30, self.rect.height)
            elif self.direction == "LEFT":
                self.attack_range = pygame.Rect(self.pos.x, self.pos.y, 30, self.rect.height)
            
            if self.attack_frame > 6:
                self.attack_frame = 0
                self.attacking = False
                self.attack_range = pygame.Rect(0, 0, 0, 0)
                return

            if self.direction == "RIGHT":
                self.image = self.attack_animation_right[self.attack_frame]
            elif self.direction == "LEFT":
                self.image = self.attack_animation_left[self.attack_frame]

            self.attack_counter += 1
            if self.attack_counter >= 3:
                self.attack_frame += 1
                self.attack_counter = 0

    def fireball(self, group):
        if self.mana >= 10:
            fireball = Fireball(self.direction, self.rect.center)
            group.add(fireball)
            self.mana -= 10

    def update(self, group, enemyProjectiles):
        self.walking()
        self.move()
        self.attack()
        #############################################################
        ####################### PHASE 2 #############################
        #############################################################
        # Always update dash
        
        self.dash()
        self.defend()

        #############################################################
        ####################### PHASE 2 #############################
        #############################################################
        self.collision(group)
        self.checkProjectiles(enemyProjectiles)

    def checkProjectiles(self, group):
        hits = pygame.sprite.spritecollideany(self, group)
        if hits:
            self.player_hit(1)

    def player_hit(self, damage):
        if self.hit_cooldown == False:
            self.hit_cooldown = True
            self.healthBar.takeDamage(damage)
            pygame.time.set_timer(self.hit_cooldown_event, 1000)


    def collision(self, group):

        hits = pygame.sprite.spritecollide(self, group, False)

        if self.vel.y > 0:
            if hits:
                lowest = hits[0]

                if self.rect.bottom >= lowest.rect.top:
                    self.pos.y = lowest.rect.top - self.rect.height
                    self.rect.y = lowest.rect.top - self.rect.height 
                    self.vel.y = 0
                    self.jumping = False

    def jump(self):
        if self.jumping == False:
            self.jumping = True
            self.vel.y = -12

    def jump_cancel(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def incMana(self, n):
        if self.mana + n <= self.maxMana:
            self.mana += n
        else:
            self.mana = self.maxMana

    def useManaPotion(self):
        if self.mana == self.maxMana:
            return
        
        if self.manaPotions >= 1:
            self.manaPotions -= 1
            if self.mana + 50 > self.maxMana:
                self.mana = self.maxMana
            else:
                self.mana += 50


    def render(self, display):
        #pygame.draw.rect(display, (255, 0, 0), self.rect)
        #pygame.draw.rect(display, (0, 255, 0), self.attack_range)
        display.blit(self.image, self.pos)
        self.healthBar.render(display)
        pygame.draw.rect(display, (0,0,255), pygame.Rect(self.pos.x, self.rect.y - 50,
                                                         100 * (self.mana/self.maxMana), 15))

    def load_animations(self):
        self.animation_right = [pygame.image.load("Images/Player_Sprite_R.png").convert_alpha(),
                   pygame.image.load("Images/Player_Sprite2_R.png").convert_alpha(),
                   pygame.image.load("Images/Player_Sprite3_R.png").convert_alpha(),
                   pygame.image.load("Images/Player_Sprite4_R.png").convert_alpha(),
                   pygame.image.load("Images/Player_Sprite5_R.png").convert_alpha(),
                   pygame.image.load("Images/Player_Sprite6_R.png").convert_alpha(),
                   pygame.image.load("Images/Player_Sprite_R.png").convert_alpha()]

        self.animation_left = [pygame.image.load("Images/Player_Sprite_L.png").convert_alpha(),
                          pygame.image.load("Images/Player_Sprite2_L.png").convert_alpha(),
                          pygame.image.load("Images/Player_Sprite3_L.png").convert_alpha(),
                          pygame.image.load("Images/Player_Sprite4_L.png").convert_alpha(),
                          pygame.image.load("Images/Player_Sprite5_L.png").convert_alpha(),
                          pygame.image.load("Images/Player_Sprite6_L.png").convert_alpha(),
                          pygame.image.load("Images/Player_Sprite_L.png").convert_alpha()]

        self.attack_animation_right = [pygame.image.load("Images/Player_Sprite_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack1_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack2_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack3_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack4_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack5_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Sprite_R.png").convert_alpha()]

        self.attack_animation_left = [pygame.image.load("Images/Player_Sprite_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack1_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack2_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack3_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack4_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack5_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Sprite_L.png").convert_alpha()]
        #############################################################
        ####################### PHASE 2 #############################
        #############################################################
        self.dash_animation_right = [pygame.image.load("Images/Player_Sprite_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack1_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack2_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack3_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack4_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack5_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack1_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack2_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack3_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack4_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack5_R.png").convert_alpha(),]
        
        self.dash_animation_left = [pygame.image.load("Images/Player_Sprite_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack1_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack2_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack3_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack4_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack5_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Sprite_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack1_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack2_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack3_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack4_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Attack5_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Sprite_L.png").convert_alpha()]
        
        self.defend_animation_left = [pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_L.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Sprite_L.png").convert_alpha()]
        
        self.defend_animation_right = [pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Defend_R.png").convert_alpha(),
                                  pygame.image.load("Images/Player_Sprite_R.png").convert_alpha()]


    def dash(self):
        if self.mana < 20:
            self.dashing = False
        
        if self.dashing == True:
            
            # ipdb.set_trace()
            if self.direction == "RIGHT":
                self.attack_range = pygame.Rect(self.rect.x + self.rect.width,self.pos.y, 30, self.rect.height)
            elif self.direction == "LEFT":
                self.attack_range = pygame.Rect(self.pos.x, self.pos.y, 30, self.rect.height)

            if self.dash_frame > 10:
                # print(self.attach_frame)
                self.dash_frame = 0
                self.dashing = False
                self.attack_range = pygame.Rect(0, 0, 0, 0)
                self.mana -= 20 #mana decrease
                return
            
            if self.direction == "RIGHT":
                self.image = self.dash_animation_right[self.dash_frame]
            elif self.direction == "LEFT":
                self.image = self.dash_animation_left[self.dash_frame]

            self.dash_counter += 1
            if self.dash_counter >= 2:
                self.dash_frame += 1
                self.dash_counter = 0
    

    def defend(self):
        if self.mana < 10:
            self.defending = False
            
        if self.defending == True:
            self.hit_cooldown = True    # Invincibility
            if self.defend_frame > 10:
                self.defend_frame = 0
                self.defending = False
                self.mana -= 10 #mana decrease
                self.hit_cooldown = False       # Disable Invincibility 
                return
            
            if self.direction == "RIGHT":
                try:
                    self.image = self.defend_animation_right[self.defend_frame]
                except:
                    ipdb.set_trace()
            elif self.direction == "LEFT":
                self.image = self.defend_animation_left[self.defend_frame]

            self.defend_counter += 1
            if self.defend_counter >= 2:
                self.defend_frame += 1
                self.defend_counter = 0
    

#############################################################
####################### PHASE 2 #############################
#############################################################