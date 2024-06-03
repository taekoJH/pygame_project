import pygame
from Level import Level
from Ground import Ground
from Building import Building


class LevelManager:
    def __init__(self):

        self.levels = []
        self.level = 0
        self.generatedEnemies = 0
        
        self.enemy_generation = pygame.USEREVENT + 2
        self.enemyGroup = pygame.sprite.Group()

        # Level 0 
        L0 = Level()
        L0.addGround(Ground(900, 120, -20, 340, "Images/Ground.png"))
        L0.addBuilding(Building(50, 200, "Images/Building04.png"))
        self.levels.append(L0)


        # Level 1
        L1 = Level()
        L1.addGround(Ground(900, 120, -20, 340, "Images/Ground.png"))
        L1.addBuilding(Building(500, 120, "Images/Building01.png"))
        self.levels.append(L1)


        # Level 2
        L2 = Level(5)
        L2.addGround(Ground(900, 120, -20, 340, "Images/Ground.png"))
        L2.addGround(Ground(100, 20, 300, 200, "Images/Ground.png"))
        L2.addGround(Ground(120, 20, 100, 150, "Images/Ground.png"))
        L2.addGround(Ground(80, 20, 500, 100, "Images/Ground.png"))
        self.levels.append(L2)

        # Level 3
        L3 = Level(10)
        L3.addGround(Ground(900, 120, -20, 340, "Images/Ground.png"))
        L3.addGround(Ground(100, 20, 200, 200, "Images/Ground.png"))
        L3.addGround(Ground(120, 20, 300, 120, "Images/Ground.png"))
        L3.addGround(Ground(80, 20, 400, 200, "Images/Ground.png"))
        self.levels.append(L3)


    def getLevel(self):
        return self.level

    def nextLevel(self):
        self.level += 1

    def changeLevel(self, n):
        self.level = n
        self.generatedEnemies = 0
        self.enemyGroup.empty()
        pygame.time.set_timer(self.enemy_generation, 2000) 

    def update(self):
        if (self.generatedEnemies == self.levels[self.getLevel()].enemyCount):
            pygame.time.set_timer(self.enemy_generation, 0)

