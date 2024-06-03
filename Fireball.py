import pygame



class Fireball(pygame.sprite.Sprite):
    def __init__(self,direction, position):
        super().__init__()

        self.image = None
        self.direction = direction
        
        if self.direction == "RIGHT":
            self.image = pygame.image.load("Images/fireball1_R.png")
        elif self.direction == "LEFT":
            self.image = pygame.image.load("Images/fireball1_L.png")

        self.rect = self.image.get_rect(center = position)

    def render(self, display):
        display.blit(self.image, self.rect)

    def update(self, group):
        hits = pygame.sprite.spritecollideany(self, group)
        if hits:
            self.kill()

        if self.direction == "RIGHT":
            self.rect.move_ip(3, 0)
        elif self.direction == "LEFT":
            self.rect.move_ip(-3, 0)


        
