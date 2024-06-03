import pygame



class Fireball(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()

        self.direction = player.direction
        self.image = None
        
        if self.direction == "RIGHT":
            self.image = pygame.image.load("Images/fireball1_R.png")
        elif self.direction == "LEFT":
            self.image = pygame.image.load("Images/fireball1_L.png")

        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center

    def render(self, display):
        display.blit(self.image, self.rect)

    def update(self, group):
        if pygame.sprite.spritecollideany(self, group):
            self.kill()

        if (self.rect.centerx > 850 or self.rect.centerx < 0):
            self.kill()
        else:
            if self.direction == "RIGHT":
                self.rect.move_ip(3, 0)
            elif self.direction == "LEFT":
                self.rect.move_ip(-3, 0)


        
