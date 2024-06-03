import pygame



health_animations = [pygame.image.load("Images/heart0.png"),
                     pygame.image.load("Images/heart.png"),
                     pygame.image.load("Images/heart2.png"),
                     pygame.image.load("Images/heart3.png"),
                     pygame.image.load("Images/heart4.png"),
                     pygame.image.load("Images/heart5.png")]



vec = pygame.math.Vector2


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.health = 5

        self.pos = vec(x, y)
        self.image = health_animations[self.health]

    def render(self, display):
        display.blit(self.image, self.pos)

    def takeDamage(self, damage):
        self.health -= damage
        if self.health < 0: self.health = 0
        
        self.image = health_animations[self.health]
        
    def Heal(self, heal):
        self.health += damage
        if self.health > 5: self.health = 5
        
        self.image = self.health_animations[self.health]

    

        
        
        
