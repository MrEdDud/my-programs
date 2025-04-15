import pygame

class Player:
    def __init__(self, x, y, TILE_SIZE):
        self.rect = pygame.Rect((x, y, TILE_SIZE, TILE_SIZE))  # Creating a player rectangle
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw_player(self, screen):
        pygame.draw.rect(screen, (214, 40, 40), self.rect)  # Drawing the player