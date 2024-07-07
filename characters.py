import pygame

class Pj():
    def __init__(self, x,y):
        self.rect = pygame.Rect((x,y,80,200))
        self.jump_vel = 0
        self.jump=False
        self.orientation = "right"
        self.rect = pygame.Rect((x,y,80,200))
        self.health = 310


    def move(self, screen_width, screen_height,screen,target):
        SPEED = 15
        GRAVITY = 2
        dx = 0
        dy = 0

        #Key Pressed
        key = pygame.key.get_pressed()

        #Movement
        if key[pygame.K_a]:
            dx-=SPEED

        if key[pygame.K_d]:
            dx+=SPEED

        #Jump
        if key[pygame.K_w] and self.jump==False:
            self.jump_vel = -30
            self.jump=True
        
        self.jump_vel += GRAVITY
        dy += self.jump_vel
            
        #Attack
        if key[pygame.K_j]:
            self.attack_punch(screen, (200,0,0), target)
        if key[pygame.K_k]:
            self.attack_lowkick(screen,(200,0,0),target)

        #Margin
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 40:
            self.jump_vel = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom

        #Update Player
        self.rect.x += dx
        self.rect.y += dy
                
    def attack_lowkick(self,screen, color, target):
            atacking_rect= pygame.draw.rect(screen,color,(self.rect.x+80,self.rect.y+160,40,40))
            if atacking_rect.colliderect(target.rect):
                target.health -= 15
    def attack_punch(self,screen,color,target):
            atacking_rect= pygame.draw.rect(screen,color,(self.rect.x+80,self.rect.y+40,40,40))   
            if atacking_rect.colliderect(target.rect):
                target.health -= 5
        

    def draw(self, surf):
        pygame.draw.rect(surf, (0,0,200),self.rect)
        