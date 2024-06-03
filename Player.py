import pygame
from pygame.locals import *

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.pos = vec(x, y)
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)

        self.ACC = 0.4
        self.FRIC = -0.1

        self.image = pygame.image.load("Images/Player_Sprite_R.png")


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
        


    def render(self, display):
        display.blit(self.image, self.pos)
