import pygame

class Pj():
    def __init__(self, x,y):
        self.rect = pygame.Rect((x,y,80,200))
        self.jump_vel = 0
        self.jump=False
        self.orientation = "left"
        self.rect = pygame.Rect((x,y,80,200))
        self.health = 310
        self.attacking = False

    def move(self, screen_width, screen_height,screen,target):
        SPEED = 15
        GRAVITY = 2
        dx = 0
        dy = 0

        #Key Pressed
        key = pygame.key.get_pressed()

        #If not attacking the player can move
        if self.attacking == False:
            #Movement
            if key[pygame.K_a] and key[pygame.K_j]==False  and key[pygame.K_k]==False:
                dx-=SPEED

            if key[pygame.K_d] and key[pygame.K_j]==False  and key[pygame.K_k]==False:
                dx+=SPEED

            #Jump
            if key[pygame.K_w] and self.jump==False:
                self.jump_vel = -30
                self.jump=True

            #Attacks
            if key[pygame.K_j]:
                if self.orientation=="left":
                    self.attack_punch(screen, (200,0,0), target)
                else:    
                    self.attack_punch(screen, (200,0,0), target)
    
            if key[pygame.K_k]:
                self.attack_lowkick(screen,(200,0,0),target)
        #If not attacking
        self.attacking = False

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
       
    def attack_lowkick(self,screen, color, target):
            orientation = self.orientation
            if orientation == "left":
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x+80,self.rect.y+160,40,40))
            else:
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x-40,self.rect.y+160,40,40))
            if atacking_rect.colliderect(target.rect) and target.health > 0:
                target.health -= 15
            self.attacking = True
                
    def attack_punch(self,screen,color,target):    
            orientation = self.orientation
            if orientation == "left":
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x+80,self.rect.y+40,40,40)) 
            else:
                atacking_rect= pygame.draw.rect(screen,color,(self.rect.x-40,self.rect.y+40,40,40))   
            if atacking_rect.colliderect(target.rect) and target.health > 0:
                target.health -= 5
            self.attacking = True
                
    def draw(self, surf):
        pygame.draw.rect(surf, (0,0,200),self.rect)
        