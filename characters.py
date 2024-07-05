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
        
        print(self.rect.x)
        
    def attack_lowkick(self,screen_,red_,left=False):
        
        if left==True:
        
            juan = pygame.draw.rect(screen_,red_,(self.rect.x-40,self.rect.y+160,40,40))
        else:
            juan = pygame.draw.rect(screen_,red_,(self.rect.x+80,self.rect.y+160,40,40))
            
        return juan
    def attack_punch(self,screen_,red_,left=False):
        
        if left==True:
        
            juan2 = pygame.draw.rect(screen_,red_,(self.rect.x-40,self.rect.y+40,40,40))
        
        else:
            juan2 = pygame.draw.rect(screen_,red_,(self.rect.x+80,self.rect.y+40,40,40))
        return juan2   
        

    def draw(self, surf):
        pygame.draw.rect(surf, (0,0,200),self.rect)
        