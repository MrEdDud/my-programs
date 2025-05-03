import pygame, json
from pytmx.util_pygame import load_pygame
from player import Player
pygame.init()

class Tile(pygame.sprite.Sprite):
     def __init__(self, pos, surf, groups):
          super().__init__(groups)
          self.image = surf
          self.rect = self.image.get_rect(topleft = pos)

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(SCREEN_WIDTH / 2)
        y = -target.rect.centery + int(SCREEN_HEIGHT / 2)

        x = min(0, x)  
        y = min(0, y)  
        x = max(-(self.width - SCREEN_WIDTH), x) 
        y = max(-(self.height - SCREEN_HEIGHT), y) 

        self.camera = pygame.Rect(x, y, self.width, self.height)

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

tmx_data = load_pygame("graphics/tiled/level_one.tmx")
tile_width, tile_height = tmx_data.tilewidth, tmx_data.tileheight

all_tiles = pygame.sprite.Group()
solid_tiles = pygame.sprite.Group()
killing_tiles = pygame.sprite.Group()

for layer in tmx_data.layers:
     if hasattr(layer, "data"):
        for x, y, surf in layer.tiles():
            pos = (x * tile_width, y * tile_height)
            tile_obj = Tile(pos=pos, surf=surf, groups=all_tiles)
            if layer.name == "Ground":
                 solid_tiles.add(tile_obj)
            if layer.name == "Kill":
                 killing_tiles.add(tile_obj)

camera = Camera(tmx_data.width * tmx_data.tilewidth, tmx_data.height * tmx_data.tileheight)
player = Player(50, 400, SCREEN_WIDTH, SCREEN_HEIGHT, tmx_data.height * tile_height, tmx_data.width * tile_width)

def save_and_quit():
    if event.type == pygame.QUIT:
            pygame.quit()
            exit()

while True:
    for event in pygame.event.get():
        save_and_quit()
    
    player.keys_pressed()
    player.collisions(solid_tiles, killing_tiles)
    camera.update(player)

    screen.fill((0, 0, 0))

    for tile in all_tiles:
         screen.blit(tile.image, camera.apply(tile))

    screen.blit(player.surface, camera.apply(player))
    
    pygame.display.update()
    clock.tick(60)
    