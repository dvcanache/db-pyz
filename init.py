import pygame

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Juego de Peleas")

run = True
while run:
    # Maneja eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

 
    pygame.display.flip()