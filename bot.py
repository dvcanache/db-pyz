import pygame

class Bot():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x,y,80,200))
        self.health = 310

    def draw(self, surf):
        pygame.draw.rect(surf, (0,200,0),self.rect)