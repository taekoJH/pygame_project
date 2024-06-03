import pygame


vec = pygame.math.Vector2

class Ground(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, name):

        self.image = pygame.image.load(name)

        self.size = vec(width, height)
        self.pos = vec(x, y)

    def render(self, display):
        display.blit(self.image, self.pos)
        