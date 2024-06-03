import pygame
from InventorySlot import InventorySlot

class Inventory:
    def __init__(self, player):
        self.slots = []

        self.image = pygame.image.load("Images/Inventory.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 350)

        self.playerInfo = player

        self.slots.append(InventorySlot("Images/coinIcon.png", (10, 360)))
        self.slots.append(InventorySlot("Images/manapotionIcon.png", (110, 360)))

    def update(self):
        self.slots[0].count = self.playerInfo.coins
        self.slots[1].count = self.playerInfo.manaPotions

        
    def render(self, display):
        display.blit(self.image, self.rect) 
        for slot in self.slots:
            slot.render(display)

        
