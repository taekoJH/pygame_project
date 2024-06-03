import pygame
from pygame.locals import *
import sys


from Ground import Ground
from Player import Player
from Enemy import Enemy
from UserInterface import UserInterface
from LevelManager import LevelManager


# Begin Pygame
pygame.init()


WIDTH = 800
HEIGHT = 400
FPS = 60
CLOCK = pygame.time.Clock()


display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame RPG")

background = pygame.image.load("Images/Background.png")

player = Player(200, 200)
player.load_animations()
UI = UserInterface()

Items = pygame.sprite.Group()
Projectiles = pygame.sprite.Group()

levelManager = LevelManager()


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == player.hit_cooldown_event:
            player.hit_cooldown = False
            pygame.time.set_timer(player.hit_cooldown_event, 0)

        if event.type == levelManager.enemy_generation:
            enemy = Enemy()
            levelManager.enemyGroup.add(enemy)
            levelManager.generatedEnemies += 1

        if event.type == MOUSEBUTTONDOWN:
            pass

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.jump()
            if event.key == K_RETURN:
                player.attacking = True
                player.attack()
            if event.key == K_h:
                UI.toggleInventory()
            if event.key == K_1:
                levelManager.changeLevel(0)
            if event.key == K_2:
                levelManager.changeLevel(1)
            if event.key == K_3:
                levelManager.changeLevel(2)
            if event.key == K_4:
                levelManager.changeLevel(3)
            if event.key == K_m:
                if player.mana >= 10:
                    player.fireball(Projectiles)
                    player.mana -= 10
            if event.key == K_n:
                player.incMana(5)
            if event.key == K_p:
                player.useManaPotion()

        if event.type == KEYUP:
            if event.key == K_SPACE:
                player.jump_cancel()


    # Update Functions
    for enemy in levelManager.enemyGroup:
        enemy.update(levelManager.levels[levelManager.getLevel()].groundData, player, Items)
        
    player.update(levelManager.levels[levelManager.getLevel()].groundData)
    UI.update(CLOCK.get_fps())
    
    levelManager.update()

    # Render Functions
    display.blit(background, (0, 0))

    for data in levelManager.levels[levelManager.getLevel()].data:
        data.render(display)

    for enemy in levelManager.enemyGroup:
        enemy.render(display)
    
    for item in Items:
        item.render(display)
        item.update(player, UI.inventory.slots[0])

    for projectile in Projectiles:
        projectile.render(display)
        projectile.update(levelManager.enemyGroup)
        
    player.render(display)
    UI.render(display)

    pygame.display.update()
    CLOCK.tick(FPS)