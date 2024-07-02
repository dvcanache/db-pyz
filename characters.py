import pygame

class Pj():
    def __init__(self, x,y):
        self.rect = pygame.Rect((x,y,80,200))

    def move(self, screen_width):
        SPEED = 15
        dx = 0
        dy = 0

        #Key Pressed
        key = pygame.key.get_pressed()

        #Movement
        if key[pygame.K_a]:
            dx-=SPEED

        if key[pygame.K_d]:
            dx+=SPEED

        #Margin

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        #Update Player
        self.rect.x += dx
        self.rect.y += dy


    def draw(self, surf):
        pygame.draw.rect(surf, (0,0,200),self.rect)