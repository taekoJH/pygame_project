import pygame



class InventorySlot:
    def __init__(self, name, pos):

        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.font = pygame.font.Font("Fonts/Frostbite.ttf", 25)
        self.count = 0


    def render(self, display):
        display.blit(self.image, self.rect)

        text = self.font.render(str(self.count), True, (0, 0, 0))
        display.blit(text, self.rect.midright)
        
        
