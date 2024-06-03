import pygame
from pygame.locals import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.pos = vec(x, y)
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)

        self.ACC = 0.4
        self.FRIC = -0.1

        self.image = pygame.image.load("Images/Player_Sprite_R.png")
        self.rect = self.image.get_rect()

        self.rect.topleft = self.pos


    def move(self):

        self.acc = vec(0, 0)

        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.acc.x = -self.ACC
        if keys[K_RIGHT]:
            self.acc.x = self.ACC

        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        self.rect.topleft = self.pos


    def collision(self, group):

        hits = pygame.sprite.spritecollide(self, group, False)

        if self.vel.y > 0:
            if hits:
                lowest = hits[0]

                if self.rect.bottom >= lowest.rect.top:
                    self.pos.y = lowest.rect.top - self.rect.height
                    self.rect.y = lowest.rect.top - self.rect.height 
                    self.vel.y = 0


    def render(self, display):
        display.blit(self.image, self.pos)
