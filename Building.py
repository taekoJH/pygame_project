import pygame

vec = pygame.math.Vector2

class Building(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()

        self.image = pygame.image.load(name)     
        self.rect = self.image.get_rect()

        self.pos = vec(x, y)
        self.rect.topleft = self.pos

    def render(self, display):
        display.blit(self.image, self.pos)
