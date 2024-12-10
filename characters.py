import pygame

class Pj():
    def __init__(self, x,y):
        self.rect = pygame.Rect((x,y,80,200))
        self.jump_vel = 0
        self.jump=False
        self.orientation = "left"
        self.rect = pygame.Rect((x,y,80,200))
        self.health = 310
        self.attacking = [pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_u,pygame.K_i,pygame.K_o,0]
        self.attackingCheck = False
    def move(self, screen_width, screen_height, screen, target):
        """
        Moves the player based on user input and collisions.

        Args:
            screen_width (int): The width of the screen.
            screen_height (int): The height of the screen.
            screen (pygame.Surface): The game screen.
            target (Pj or Bot): The target to move towards.
        """
        SPEED = 15
        GRAVITY = 2
        dx = 0
        dy = 0

        # Get the key pressed
        key = pygame.key.get_pressed()

        # Check if any attacking keys are pressed
        for i in range(0,7):
            if key[self.attacking[i]]:
                self.attackingCheck = True
                break
            else:
                self.attackingCheck = False

        # If not attacking, move the player
        if key[pygame.K_a] and self.attackingCheck==False:
            dx-=SPEED

            if key[pygame.K_d] and self.attacking_check==False:
                dx+=SPEED


        # Jump if the jump key is pressed and the player is not already jumping
        if key[pygame.K_w] and self.jump==False:
            self.jump_vel = -30
            self.jump=True

        # Attack if the attacking key is pressed
        if key[pygame.K_j]:
            if self.orientation=="left":
                self.attack_punch(screen, (200,0,0), target)
            else:
                self.attack_punch(screen, (200,0,0), target)

        if key[pygame.K_k]:
            self.attack_lowkick(screen,(200,0,0),target)

        # Apply gravity
        self.jump_vel += GRAVITY
        dy += self.jump_vel

        # Margin to prevent the player from moving out of the screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 40:
            self.jump_vel = 0
            self.jump = False
            dy = screen_height - 40 - self.rect.bottom

        # Update the player's orientation based on the target's position
        if self.rect[0]	> target.rect[0]:
            self.orientation = "right"
        else:
            self.orientation = "left"

        # Update the player's position
        self.rect.x += dx
        self.rect.y += dy
        
    def attacks(self, keys, screen, target):
        
        self.block = True

        if keys >=106 and keys <=108:     
            
            dmg = keys-105
            self.attack_lowkick(screen, (200,0,0), target,dmg)
            self.attacking_check = True
        else:
            self.attack_punch(screen, (200,0,0), target)
            self.attacking_check = True       
                
        
       
    def attack_lowkick(self, screen, color, target):
        # Determine the orientation of the attack
        orientation = self.orientation

        # Calculate the position of the attack
        if orientation == "left":
            attack_rect_x = self.rect.x + 80
        else:
            attack_rect_x = self.rect.x - 40
        attack_rect_y = self.rect.y + 160 + self.jump_vel

        # Draw the attack rectangle and check for collision
        attacking_rect = pygame.draw.rect(screen, color, (attack_rect_x, attack_rect_y, 40, 40))
        if attacking_rect.colliderect(target.rect) and target.health > 0:
            target.health -= 15
            
    def attack_punch(self, screen, color, target):
        # Determine the orientation of the attack
        orientation = self.orientation

        # Calculate the position of the attack
        if orientation == "left":
            attack_rect_x = self.rect.x + 80
        else:
            attack_rect_x = self.rect.x - 40
        attack_rect_y = self.rect.y + 40 + self.jump_vel

        # Draw the attack rectangle and check for collision
        attacking_rect = pygame.draw.rect(screen, color,
                                          (attack_rect_x, attack_rect_y, 40, 40))
        if attacking_rect.colliderect(target.rect) and target.health > 0:
            # Reduce the target's health by 5 if the attack is successful
            target.health -= 5
            
    def draw(self, surf):
        pygame.draw.rect(surf, (0,0,200),self.rect)
        