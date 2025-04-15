import pygame

class Player:
    def __init__(self, x, y, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.surface = pygame.Surface((50,50))
        self.surface.fill((255, 0, 0))
        self.rect = self.surface.get_rect(center = (x, y))
        
        self.speed = 5
        self.gravity = 0.4
        self.vertical_speed = 0
        self.is_jumping = False

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def _gravity(self):
        self.vertical_speed += self.gravity
        self.move(0, self.vertical_speed)

    def event_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.vertical_speed = -10
            self.is_jumping = True
        if keys[pygame.K_a]:
            self.move(-self.speed, 0)
        if keys[pygame.K_d]:
            self.move(self.speed, 0)
    
    def collisions(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            self.is_jumping = False
            self.vertical_speed = 0
    
    def draw(self, screen):
        screen.blit(self.surface, self.rect)