import pygame

class Pj():
    def __init__(self, x,y):
        self.rect = pygame.Rect((x,y,80,200))
        self.jump_vel = 0
        self.jump=False
        self.orientation = "left"
        self.rect = pygame.Rect((x,y,80,200))
        self.health = 310
        self.attacking_keys = [pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_u,pygame.K_i,pygame.K_o,0]
        self.attacking_check = False
        self.attack_delay = pygame.time.Clock()
        self.block = False
    def move(self, screen_width, screen_height,screen,target,):
        SPEED = 15
        global GRAVITY
        GRAVITY = 2
        dx = 0
        dy = 0

        #Key Pressed
        key = pygame.key.get_pressed()        
        
        # checking attack keys
        
    
       # for i in range(0,7):
            
       #     if key[self.attacking_keys[i]]:
                
       #         print(self.attacking_keys)
                
       #         self.attacking_check = True
       #         break
       #     else:
       #        self.attacking_check = False

        #If not attacking the player can move
        
        #Movement
        if self.block == False:
        
            if key[pygame.K_a] and self.attacking_check==False:
                dx-=SPEED

            if key[pygame.K_d] and self.attacking_check==False:
                dx+=SPEED

        #Jump
        if key[pygame.K_w] and self.jump==False:
            self.jump_vel = -30
            self.jump=True

        #Attacks
        if key[pygame.K_j]:
            self.attack_punch(screen, (200,0,0), target)
            

        if key[pygame.K_k]:
            self.attack_lowkick(screen,(200,0,0),target)

        #Gravity
        self.jump_vel += GRAVITY
        dy += self.jump_vel 

        #Margin
        if self.rect.left + dx < 0:
            dx = -self.rect.left
            
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
            
        if self.rect.bottom + dy > screen_height - 40:
            self.jump_vel = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom
  
        if self.rect[0]	> target.rect[0]:
            self.orientation = "right"
        else:
            self.orientation = "left"

        #Update Player
        self.rect.x += dx
        self.rect.y += dy
        
    def attacks(self, keys, screen, target):
        
        self.block = True

        key = pygame.key.get_pressed()        
        
        # checking attack keys
        #for i in range(0,7):
           # if keys == self.attacking_keys[i]:
                
                
                
                
        self.attack_lowkick(screen, (200,0,0), target)
        self.attacking_check = True
                
                
        
    def attack_lowkick(self,screen, color, target):
            orientation = self.orientation
            if orientation == "left":
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x+80,self.rect.y+160+self.jump_vel,40,40))
            else:
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x-40,self.rect.y+160+self.jump_vel,40,40))
            if atacking_rect.colliderect(target.rect) and target.health > 0:
                target.health -= 2
            
    def attack_punch(self,screen,color,target):    
            orientation = self.orientation
            if orientation == "left":
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x+80,self.rect.y+40+self.jump_vel,40,40)) 
            else:
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x-40,self.rect.y+40+self.jump_vel,40,40))   
            if atacking_rect.colliderect(target.rect) and target.health > 0:
                target.health -= 3
            
    def draw(self, surf):
        pygame.draw.rect(surf, (0,0,200),self.rect)
        