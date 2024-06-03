import pygame
from Inventory import Inventory

class UserInterface:
    def __init__(self):
        self.color_red = (255, 0, 0)
        self.color_green = (0, 255, 0)
        self.color_blue = (0, 0, 255)
        self.color_black = (0, 0, 0)
        self.color_white = (255, 255, 255)

        self.smallfont = pygame.font.SysFont("Verdana", 12)
        self.regularfont = pygame.font.SysFont("Verdana", 20)
        self.largefont = pygame.font.SysFont("Verdana", 40)

        self.playerRef = player

        self.text = self.regularfont.render("0", True, self.color_black)
        self.inventory = Inventory(player)
        self.inventoryRender = True


    def update(self, fps):
        self.text = self.regularfont.render(str(fps), True, self.color_black)
        self.inventory.update()
        
    def render(self, display):
        display.blit(self.text, (700, 20))

        if self.showInventory:
            self.inventory.render(display)


    def toggleInventory(self):
        if self.showInventory:
            self.showInventory = False
        else:
            self.showInventory = True