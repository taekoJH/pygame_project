import pygame
from InventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []

        self.image = pygame.image.load("Images/Inventory.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 350)

        self.slots.append(InventorySlot("Images/coinIcon.png", (20, 360)))
        self.slots.append(InventorySlot("Images/manapotionIcon.png", (120, 360)))

        
    def render(self, display):
        display.blit(self.image, (0, 350)) 
        for slot in self.slots:
            slot.render(display)

        
