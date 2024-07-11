import pygame
from characters import Pj
from bot import Bot

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
algo = False
perro = 0
block = False
permitir = False
while run:
    # Time manager
    sec += timer.tick(fps)   
    tempo_bend = txt.render(tempo, True, black)
    #Drawing
    draw_bg()

    #Player control
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            
            if pygame.key.get_pressed()[pygame.K_l] and block == False and permitir == True:              
                algo = True
                stop = True
        if algo == False:        
                
            if pygame.KEYUP and pygame.key.get_pressed()[pygame.K_l]==False:
                    
                permitir = True         
    if algo == True:   
        perro += 16    
        if perro < 200:        
            permitir = False
            pj.attacks(pygame.K_l,screen, bot)
        else:
            pj.attacking_check = False
            algo = False   
            perro = 0
            pj.block = False 
                
                
            
    print(sec)        
             
        
    pj.move(WINDOW_WIDTH, WINDOW_HEIGHT, screen, bot)
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
