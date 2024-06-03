import pygame
from pygame.locals import *
import sys


from Ground import Ground
from Player import Player
from Enemy import Enemy
from UserInterface import UserInterface


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
player = Player(200, 200)
player.load_animations()
UI = UserInterface()

ground2 = Ground(100, 20, 300, 200, "Images/Ground.png")
ground3 = Ground(120, 20, 100, 150, "Images/Ground.png")
ground4 = Ground(80, 20, 500, 100, "Images/Ground.png")

EnemyGroup = pygame.sprite.Group()


GroundGroup = pygame.sprite.Group()
GroundGroup.add(ground)
GroundGroup.add(ground2)
GroundGroup.add(ground3)
GroundGroup.add(ground4)

Items = pygame.sprite.Group()

enemy_generation = pygame.USEREVENT + 2

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == player.hit_cooldown_event:
            player.hit_cooldown = False
            pygame.time.set_timer(player.hit_cooldown_event, 0)

        if event.type == MOUSEBUTTONDOWN:
            pass

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.jump()
            if event.key == K_RETURN:
                player.attacking = True
                player.attack()
            if event.key == K_q:
                pygame.time.set_timer(enemy_generation, 2000)
            if event.key == K_w:
                pygame.time.set_timer(enemy_generation, 0)

        if event.type == KEYUP:
            if event.key == K_SPACE:
                player.jump_cancel()


    # Update Functions
    for enemy in EnemyGroup:
        enemy.update(GroundGroup, player)
        
    player.update(GroundGroup)
    UI.update(CLOCK.get_fps())


    # Render Functions
    display.blit(background, (0, 0))
    player.render(display)
    UI.render(display)

    for item in Items:
        item.render(display)
        item.update(player)
    
    for grounds in GroundGroup:
        grounds.render(display)

    for enemy in EnemyGroup:
        enemy.render(display)


    pygame.display.update()
    CLOCK.tick(FPS)