import pygame
import random
import numpy
from Item import Item
from Fireball import Fireball

vec = pygame.math.Vector2


class RangedEnemy(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__()

        self.image = None
        self.direction = random.randint(0, 1) # 0 -> Means Right | 1 -> Means Left
        self.projectilesGroup = group
        
        if self.direction == 0:
            self.image = pygame.image.load("Images/enemy2.png")
            self.direction = "RIGHT"
        elif self.direction == 1:
            self.image = pygame.image.load("Images/enemy2_L.png")
            self.direction = "LEFT"
            
        self.rect = self.image.get_rect()

        self.pos = vec(random.randint(0, 800), 0)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.FRIC = -0.1
        self.ACC = round(random.uniform(0.05, 0.1), 2)
        self.attack_cooldown = 300
        self.turn_cooldown = 120

    def move(self):
        self.acc = vec(0, 0.5)

        if self.direction == "RIGHT":
            self.acc.x = self.ACC
        elif self.direction == "LEFT":
            self.acc.x = -self.ACC

        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > 780:
            self.direction = "LEFT"
            self.image = pygame.image.load("Images/enemy2_L.png")
        elif self.pos.x < 0:
            self.direction = "RIGHT"
            self.image = pygame.image.load("Images/enemy2.png")

        self.rect.topleft = self.pos


    def collision(self, group):
        hits = pygame.sprite.spritecollide(self, group, False)

        if self.vel.y > 0:
            if hits:
                lowest = hits[0]

                if self.rect.bottom >= lowest.rect.top:
                    self.pos.y = lowest.rect.top - self.rect.height
                    self.rect.y = lowest.rect.top - self.rect.height 
                    self.vel.y = 0

    def player_collision(self, player, projectiles, itemGroup):
        if self.rect.colliderect(player.attack_range) or pygame.sprite.spritecollide(self, projectiles, True):
            # Hit by the Player
            self.kill()

            random_chance = numpy.random.uniform(1, 100)

            if random_chance >= 1 and random_chance <= 10:
                item = Item(self.pos.x, self.pos.y, 0, "Images/coin.png")
                itemGroup.add(item)
            elif random_chance >= 11 and random_chance <= 20:
                item = Item(self.pos.x, self.pos.y, 1, "Images/heart1.png")
                itemGroup.add(item)
            elif random_chance >= 21 and random_chance <= 30:
                item = Item(self.pos.x, self.pos.y, 2, "Images/mana_potion.png")
                itemGroup.add(item)

            
    def update(self, groundGroup, player, projectiles, itemGroup):
        self.move()
        self.collision(groundGroup)
        self.player_collision(player,  projectiles, itemGroup)
        self.attack()
        self.turn(player)

    def attack(self):
        if self.attack_cooldown <= 0:
            fireball = Fireball(self.direction, self.rect.center)
            self.projectilesGroup.add(fireball)
            self.attack_cooldown = 300
        else:
            self.attack_cooldown -= 1

    def turn(self, player):
        if self.turn_cooldown <= 0:
            if (player.rect.centerx - self.rect.x < 0 and self.direction == "RIGHT"):
                self.direction = "LEFT"
                self.image = pygame.image.load("Images/enemy2_L.png")
            elif (player.rect.centerx - self.rect.x > 0 and self.direction == "LEFT"):
                self.direction = "RIGHT"
                self.image = pygame.image.load("Images/enemy2.png")
                
            self.turn_cooldown = 120
        else:
            self.turn_cooldown -= 1            

    def render(self, display):
        display.blit(self.image, self.pos)
        #pygame.draw.rect(display, (0, 0, 255), self.rect)


        
        
