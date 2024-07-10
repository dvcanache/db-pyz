import pygame
from characters import Pj
from bot import Bot

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Peleas")

#load resources
bg = pygame.image.load("assets/fondo_pyz.png")
health_body = pygame.image.load("assets/health_bars.png")
txt = pygame.font.Font('freesansbold.ttf', 32)

def draw_bg():
    screen.blit(bg, (0, 0))

def health_bars(health_bar_left, health_bar_right):
    # Draw the background of the health bars
    pygame.draw.rect(screen, green, (65, 30, 310, 25))
    pygame.draw.rect(screen, red, (430, 30, 310, 25))

    # Draw the health bars themselves
    pygame.draw.rect(screen, red, (65, 30, health_bar_left - 310, 25))
    pygame.draw.rect(screen, green, (430, 30, health_bar_right, 25))
    
pj = Pj(200,360)
bot = Bot(500,360)
tempo = "60"
tempoCount = 60
green =(0,255,0)
red = (255,0,0)
black=(0,0,0)
fps = 60
timer = pygame.time.Clock()
run = True
sec = 0

while run:
    # Time manager
    sec += timer.tick(fps)   
    tempo_bend = txt.render(tempo, True, black)
    #Drawing
    draw_bg()

    #P;ayer control
    pj.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, bot)
    pj.draw(screen)

    #Bot control
    bot.draw(screen)
           
    if pygame.event.get(pygame.QUIT):    
        run=False         
                
    # Time counter            
    if sec > 1000:
        sec -= 1000
        if tempoCount>0: 
            tempoCount -= 1
            tempo = str(tempoCount)

    #Health bars and tempo counter
    health_bars(pj.health, bot.health)
    screen.blit(health_body, (65, 30))
    screen.blit(health_body, (430, 30))
    screen.blit(tempo_bend, (380, 50))

    pygame.display.flip()
