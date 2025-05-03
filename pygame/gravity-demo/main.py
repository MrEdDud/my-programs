import pygame, json
from player import Player

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 680
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player(32, 32, SCREEN_WIDTH, SCREEN_HEIGHT)

"""def save(filename):
    with open(filename, "w") as f:
        json.dump(dictionary, f)

def load(filename):
    with open(filename, "r") as f:
        loading = json.load(f)
        dictionary.update(loading)

load("savegame.json")"""

def save_and_quit():
    if event.type == pygame.QUIT:
            #save("savegame.json")
            pygame.quit()
            exit()

while True:
    for event in pygame.event.get():
        save_and_quit()
    
    screen.fill("Black")
    
    player.player_input()
    player.grav()
    player.collisions()
    player.drawing(screen)
    
    pygame.display.update()
    clock.tick(60)