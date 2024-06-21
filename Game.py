import pygame
from pygame.locals import *
import sys
import random


from Ground import Ground
from Player import Player
from Enemy import Enemy
from RangedEnemy import RangedEnemy
from UserInterface import UserInterface
from LevelManager import LevelManager


import pygame
from pygame.locals import *
import sys
import random

from Ground import Ground
from Player import Player
from Enemy import Enemy
from RangedEnemy import RangedEnemy
from UserInterface import UserInterface
from LevelManager import LevelManager


#############################################################
####################### PHASE 2 #############################
#############################################################
# Add Button
class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font(None, 36)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.color = (0, 128, 0)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()

# Add reset_game function
def reset_game():
    global player, levelManager, UI, EnemyProjectiles, PlayerProjectiles, Items, game_over

    game_over = False  # Reset game over flag

    player = Player(200, 200)
    player.load_animations()
    UI = UserInterface(player)

    Items = pygame.sprite.Group()
    PlayerProjectiles = pygame.sprite.Group()
    EnemyProjectiles = pygame.sprite.Group()
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)

    levelManager = LevelManager()

#############################################################
####################### PHASE 2 #############################
#############################################################


#############################################################
####################### PHASE 2 #############################
#############################################################
# change to main function
def main():
    
    # Begin Pygame
    pygame.init()

    # global parameter
    global player, levelManager, UI, EnemyProjectiles, PlayerProjectiles, Items
    global WIDTH, HEIGHT, FPS, CLOCK, display, background, game_over

    WIDTH = 800
    HEIGHT = 400
    FPS = 60
    CLOCK = pygame.time.Clock() 

    # Initialize display
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame RPG")

    background = pygame.image.load("Images/Background.png").convert()

    player = Player(200, 200)
    player.load_animations()
    UI = UserInterface(player)

    Items = pygame.sprite.Group()
    PlayerProjectiles = pygame.sprite.Group()
    EnemyProjectiles = pygame.sprite.Group()
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)

    levelManager = LevelManager()
    
    # Buttons for game over state
    retry_button = Button(300, 200, 200, 50, "Retry", reset_game)
    quit_button = Button(300, 300, 200, 50, "Quit", pygame.quit)

    # Add game_over parameter
    game_over = False

    while True:
        # Condition to game over
        if player.healthBar.health == 0:
            game_over = True

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #############################################################
            ####################### PHASE 2 #############################
            #############################################################
            if game_over:
                retry_button.is_clicked(event)
                quit_button.is_clicked(event)
            #############################################################
            ####################### PHASE 2 #############################
            #############################################################

            if event.type == player.hit_cooldown_event:
                player.hit_cooldown = False
                pygame.time.set_timer(player.hit_cooldown_event, 0)

            if event.type == levelManager.enemy_generation:
                choice = random.randint(0, 1)
                enemy = None

                if choice == 0:
                    enemy = Enemy()
                elif choice == 1:
                    enemy = RangedEnemy(EnemyProjectiles)
                
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
                if event.key == K_1:
                    levelManager.changeLevel(0)
                if event.key == K_2:
                    levelManager.changeLevel(1)
                if event.key == K_3:
                    levelManager.changeLevel(2)
                if event.key == K_4:
                    levelManager.changeLevel(3)
                if event.key == K_h:
                    UI.toggleInventory()
                if event.key == K_m:
                    player.fireball(PlayerProjectiles)
                if event.key == K_p:
                    player.useManaPotion()
                #############################################################
                ####################### PHASE 2 #############################
                #############################################################
                # Ult skill - R
                if event.key == K_r:
                    player.dashing = True
                    player.dash()

                #  skill - E
                if event.key == K_e:
                    player.defending = True
                    player.defend()

                #############################################################
                ####################### PHASE 2 #############################
                #############################################################
                    
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    player.jump_cancel()

        # Update and render game if not game over
        if not game_over:
            for enemy in levelManager.enemyGroup:
                enemy.update(levelManager.levels[levelManager.getLevel()].groundData, player, PlayerProjectiles, Items)

            player.update(levelManager.levels[levelManager.getLevel()].groundData, EnemyProjectiles)
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
                item.update(player)

            for projectile in PlayerProjectiles:
                projectile.render(display)
                projectile.update(levelManager.enemyGroup)

            for projectile in EnemyProjectiles:
                projectile.render(display)
                projectile.update(playerGroup)

            player.render(display)
            UI.render(display)
        else:
            #############################################################
            ####################### PHASE 2 #############################
            #############################################################
            # Render game over screen with buttons
            display.fill((0, 0, 0))
            retry_button.render(display)
            quit_button.render(display)
            #############################################################
            ####################### PHASE 2 #############################
            #############################################################


        pygame.display.update()
        CLOCK.tick(FPS)

if __name__ == "__main__":
    main()


#############################################################
####################### PHASE 2 #############################
#############################################################


'''
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
UI = UserInterface(player)

Items = pygame.sprite.Group()
PlayerProjectiles = pygame.sprite.Group()
EnemyProjectiles = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
playerGroup.add(player)

levelManager = LevelManager()


while True:
    if player.healthBar.health == 0:
        pygame.quit()
        sys.exit()

    print(f"player.healthBar.health = {player.healthBar.health}")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == player.hit_cooldown_event:
            player.hit_cooldown = False
            pygame.time.set_timer(player.hit_cooldown_event, 0)

        if event.type == levelManager.enemy_generation:
            choice = random.randint(0, 1)
            enemy = None

            if choice == 0:
                enemy = Enemy()
            elif choice == 1:
                enemy = RangedEnemy(EnemyProjectiles)
                
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
            if event.key == K_1:
                levelManager.changeLevel(0)
            if event.key == K_2:
                levelManager.changeLevel(1)
            if event.key == K_3:
                levelManager.changeLevel(2)
            if event.key == K_4:
                levelManager.changeLevel(3)
            if event.key == K_h:
                UI.toggleInventory()
            if event.key == K_m:
                player.fireball(PlayerProjectiles)
            if event.key == K_p:
                player.useManaPotion()
            #############################################################
            ####################### PHASE 2 #############################
            #############################################################
            # Ult skill - R
            if event.key == K_r:
                player.dashing = True
                player.dash()

            #  skill - E
            if event.key == K_e:
                player.defending = True
                player.defend()


            #############################################################
            ####################### PHASE 2 #############################
            #############################################################

                
        if event.type == KEYUP:
            if event.key == K_SPACE:
                player.jump_cancel()


    # Update Functions
    for enemy in levelManager.enemyGroup:
        enemy.update(levelManager.levels[levelManager.getLevel()].groundData,player,PlayerProjectiles,Items)
        
    player.update(levelManager.levels[levelManager.getLevel()].groundData, EnemyProjectiles)
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
        item.update(player)

    for projectile in PlayerProjectiles:
        projectile.render(display)
        projectile.update(levelManager.enemyGroup)
    
    for projectile in EnemyProjectiles:
        projectile.render(display)
        projectile.update(playerGroup)
        
    player.render(display)
    UI.render(display)

    pygame.display.update()
    CLOCK.tick(FPS)

'''