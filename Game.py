import pygame
from pygame.locals import *
import sys


from Ground import Ground
from Player import Player

# Begin Pygame
pygame.init()


WIDTH = 800
HEIGHT = 400
FPS = 60
CLOCK = pygame.time.Clock()


display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame RPG")

background = pygame.image.load("Images/Background.png")

ground = Ground(900, 120, -20, 320, "Images/Ground.png")


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            pass

        if event.type == KEYDOWN:
            pass

    Player.move()

    display.blit(background, (0, 0))
    ground.render(display)
    player.render(display)

    pygame.display.update()
    CLOCK.tick(FPS)