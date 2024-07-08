import pygame

from bot import Bot

bot= Bot(500,360)
class Pj():
    def __init__(self, x,y):
        self.rect = pygame.Rect((x,y,80,200))
        self.jump_vel = 0
        self.jump=False
        self.orientation = ["left"]
        self.rect = pygame.Rect((x,y,80,200))
        self.health = 310


    def move(self, screen_width, screen_height,screen,target,):
        SPEED = 15
        GRAVITY = 2
        dx = 0
        dy = 0

        #Key Pressed
        key = pygame.key.get_pressed()

        #Movement
        if key[pygame.K_a] and key[pygame.K_j]==False  and key[pygame.K_k]==False:
            dx-=SPEED

        if key[pygame.K_d] and key[pygame.K_j]==False  and key[pygame.K_k]==False:
            dx+=SPEED

        #Jump
        if key[pygame.K_w] and self.jump==False:
            self.jump_vel = -30
            self.jump=True
        
        self.jump_vel += GRAVITY
        dy += self.jump_vel
            
        #Attacks
        if key[pygame.K_j]:
            
            if self.orientation[0]=="left":
                self.attack_punch(screen, (200,0,0), target)
            else:    
                self.attack_punch(screen, (200,0,0), target)
            
            
            
        if key[pygame.K_k]:
            
            
            
            self.attack_lowkick(screen,(200,0,0),target)
            #print(bot.rect[0])

        #Margin
        if self.rect.left + dx < 0:
            dx = -self.rect.left
            
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
            
        if self.rect.bottom + dy > screen_height - 40:
            self.jump_vel = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom
        
        #bot = ano()
        
        if self.rect[0]	> bot.rect[0]:
            
            del self.orientation[0]
            self.orientation.append("right")
            
        else:
            del self.orientation[0]
            self.orientation.append("left")
            
        #print(self.rect)
        #Update Player
        self.rect.x += dx
        self.rect.y += dy
        
        
    
        
    
                
    def attack_lowkick(self,screen, color, target):

            orientation = self.orientation[0]
            if orientation == "left":
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x+80,self.rect.y+160,40,40))
            else:
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x-40,self.rect.y+160,40,40))
            if atacking_rect.colliderect(target.rect) and target.health > 0:
                target.health -= 15
                
                
    def attack_punch(self,screen,color,target):
            
            orientation = self.orientation[0]
            if orientation == "left":
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x+80,self.rect.y+40,40,40)) 
            else:
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x-40,self.rect.y+40,40,40))   
            if atacking_rect.colliderect(target.rect) and target.health > 0:
                target.health -= 5
                

    def draw(self, surf):
        pygame.draw.rect(surf, (0,0,200),self.rect)
        