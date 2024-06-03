import pygame
from InventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []

        self.image = pygame.image.load("Images/Inventory.png")
        self.slots = []
        self.playerRef = player

        self.slots.append(InventorySlot("Images/coinIcon.png", (20, 360)))
        self.slots.append(InventorySlot("Images/manapotionIcon.png", (120, 360)))

    def update(self):
        self.slots[0].count = self.playerRef.coins
        self.slots[1].count = self.playerRef.manaPotions

        
    def render(self, display):
        display.blit(self.image, (0, 350)) 
        for slot in self.slots:
            slot.render(display)

        
