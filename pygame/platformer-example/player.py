import pygame

class Player:
    def __init__(self, x, y, width, height, map_height, map_width):
        self.surface = pygame.Surface((32, 32))
        self.surface.fill((31,5,211))
        self.rect = self.surface.get_rect(center=(x, y))
        self.screen_width, self.screen_height  = width, height
        self.map_width, self.map_height = map_width, map_height  
        
        self.gravity = 0.2
        self.friction = -0.6
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)
        
        self.on_ground = False
        self.LEFT_KEY, self.RIGHT_KEY = False, False


    def player_running(self):
        self.acceleration.x = 0
        if self.LEFT_KEY:
            self.acceleration.x = -3
        elif self.RIGHT_KEY:
            self.acceleration.x = 3
        
        self.acceleration.x += self.velocity.x * self.friction

        self.velocity += self.acceleration
        self.limit_velocity(5)
        self.position += self.velocity + 0.5 * self.acceleration

        self.rect.x = self.position.x
    
    def player_jumping(self):
        self.velocity.y += self.acceleration.y
        if self.velocity.y > 7:
            self.velocity.y = 7
        self.position.y += self.velocity.y + 0.5 * self.acceleration.y
        self.rect.bottom = self.position.y

    def keys_pressed(self):
        keys = pygame.key.get_pressed()
        self.LEFT_KEY = keys[pygame.K_a]
        self.RIGHT_KEY = keys[pygame.K_d]

        if keys[pygame.K_SPACE]:
            if self.on_ground:
                self.velocity.y = -8
                self.on_ground = False
    
    def limit_velocity(self, max_vel):
        if abs(self.velocity.x) > max_vel:
            self.velocity.x = max_vel if self.velocity.x > 0 else -max_vel
        if abs(self.velocity.x) < 0.01:
            self.velocity.x = 0
    
    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                hits.append(tile)
        return hits

    def check_collisions_x(self, tiles):
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.x > 0: 
                self.position.x = tile.rect.left - self.rect.width
                self.rect.x = self.position.x
            elif self.velocity.x < 0: 
                self.position.x = tile.rect.right
                self.rect.x = self.position.x
        self.velocity.x = 0

    def check_collisions_y(self, tiles):
        self.on_ground = False
        collisions = self.get_hits(tiles)
        for tile in collisions:
            if self.velocity.y > 0:
                self.position.y = tile.rect.top
                self.rect.bottom = self.position.y
                self.velocity.y = 0
                self.on_ground = True
            elif self.velocity.y < 0:
                self.position.y = tile.rect.bottom + self.rect.height
                self.rect.bottom = self.position.y
                self.velocity.y = 0

    def check_death(self, tiles):
        collisions = self.get_hits(tiles)
        if collisions:
            self.position = pygame.math.Vector2(50, 400)
            self.velocity = pygame.math.Vector2(0,0)

    def collisions(self, solid_tiles, killing_tiles):
        self.player_running()
        self.check_collisions_x(solid_tiles)
        self.player_jumping()
        self.check_collisions_y(solid_tiles)
        self.check_death(killing_tiles)
        # Left collisions
        if self.rect.left < 0:
            self.rect.left = 0
            self.position.x = self.rect.left
        # Right collisions
        if self.rect.right > self.map_width:
            self.rect.right = self.map_width
            self.position.x = self.rect.right - self.rect.width
        # Top collisions
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity.y = 2
        # Bottom collisions
        if self.rect.bottom > self.map_height:
            self.rect.bottom = self.map_height
            self.position.y = self.rect.bottom

    def drawing(self, screen):
        screen.blit(self.surface, self.rect)
