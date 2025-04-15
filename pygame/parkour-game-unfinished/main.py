import pygame, json
from pytmx.util_pygame import load_pygame
from scripts.player import Player
pygame.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

pygame.display.set_caption("Parkour Game")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
player = Player(32, 32, SCREEN_WIDTH, SCREEN_HEIGHT)

tmx_data = load_pygame("scenes/level_one.tmx")
sprite_group = pygame.sprite.Group()

for layer in tmx_data.layers:
    if hasattr(layer, "data"):
        for x, y, surf in layer.tiles():
            pos = (x * 32, y * 32)
            Tile(pos = pos, surf = surf, groups = sprite_group)

game_state = {
    "level": 0
}
# Function to save the game
def save_game_state(filename):
    with open(filename, "w") as f:
        json.dump(game_state, f)
# Function to load the game
def load_game_state(filename):
    with open(filename, "r") as f:
        loaded_state = json.load(f)
        game_state.update(loaded_state)
# Function to save and quit the game
def save_and_quit():
    if event.type == pygame.QUIT:
        save_game_state("save_data\player_save.json") # Saves the game
        pygame.quit()
        exit()

# Game loop
while True:
    for event in pygame.event.get():
        save_and_quit()
    
    sprite_group.draw(screen)

    player.event_keys()
    player._gravity()
    player.collisions()
    player.draw(screen)
    
    pygame.display.update()
    clock.tick(60)