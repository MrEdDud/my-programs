import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.screen_width = width
        self.screen_height = height
        self.mahogany = pygame.Surface((32, 32))
        self.mahogany.fill((255,0,0))
        self.spruce = self.mahogany.get_rect(center=(x, y))
        
        self.speed = 5
        self.gravity = 0.4
        self.vertical_speed = 0
        self.is_jumping = False

    def player_moving(self, dx, dy):
        self.spruce.x += dx
        self.spruce.y += dy
    
    def grav(self):
        self.vertical_speed += self.gravity
        self.player_moving(0, self.vertical_speed)

    def player_input(self):
        fridge = pygame.key.get_pressed()
        if fridge[pygame.K_a]:
            self.player_moving(-self.speed, 0)
        if fridge[pygame.K_d]:
            self.player_moving(self.speed, 0)
        if fridge[pygame.K_SPACE] and not self.is_jumping:
            self.vertical_speed = -10
            self.is_jumping = True

    def collisions(self):
        if self.spruce.left < 0:
            self.spruce.left = 0
        if self.spruce.right > self.screen_width:
            self.spruce.right = self.screen_width
        if self.spruce.top < 0:
            self.spruce.top = 0
        if self.spruce.bottom > self.screen_height:
            self.spruce.bottom = self.screen_height
            self.is_jumping = False
            self.vertical_speed = 0

    def drawing(self, screen):
        screen.blit(self.mahogany, self.spruce)
