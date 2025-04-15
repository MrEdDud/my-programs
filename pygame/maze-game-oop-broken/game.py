import pygame, json # Importing different modules
from player import Player
from menu import Menu
from maze import Maze


pygame.init() # Initialising Pygame
pygame.display.set_caption("Maze Game") # Setting the game name

SCREEN_WIDTH = 750 # Setting the screen width
SCREEN_HEIGHT = 450 # Setting the screen height
TILE_SIZE = 50 # Setting the tile size

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creating the display
        self.font = pygame.font.Font(None, 36) # Setting the font
        self.clock = pygame.time.Clock() # Initialising the clock
        self.game_state = {"level": 0} # Dictionary storing values of the player to save
        self.on_s_block = False
        self.main_menu = True

        self.player_rect = Player(TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.maze = Maze(TILE_SIZE, self.screen)
        self.menu = Menu(self.screen, self.font, self.clock, TILE_SIZE, self.game_state, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Function to save the game
    def save_game_state(self, filename):
        with open(filename, "w") as f:
            json.dump(self.game_state, f)
    # Function to load the game
    def load_game_state(self, filename):
        with open(filename, "r") as f:
            loaded_state = json.load(f)
            self.game_state.update(loaded_state)

    def switch_level(self):
        if self.game_state["level"] == 1:
            self.player_rect.rect.x = TILE_SIZE
            self.player_rect.rect.y = TILE_SIZE
            self.maze.load_level(2)

    def game_start(self):
        self.load_game_state("savegame.json")
        while True:
            new_x, new_y, self.main_menu = self.events()
            if self.main_menu:
                self.menu.main_menu_screen()
            else:
                self.update_player_postion(new_x, new_y)
                self.draw_maze()
                self.player_rect.draw_player(self.screen)
            
            pygame.display.update()
            self.clock.tick(60)

    # Event handler
    def events(self):
        x, y = 0, 0
        for event in pygame.event.get():
            # Checks if the player has quit the program
            if event.type == pygame.QUIT:
                self.save_game_state("savegame.json") # Saves the game
                pygame.quit()
                exit()
            # Checks if the player is pressing down any key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y = -TILE_SIZE
                elif event.key == pygame.K_s:
                    y = TILE_SIZE
                elif event.key == pygame.K_a:
                    x = -TILE_SIZE
                elif event.key == pygame.K_d:
                    x = TILE_SIZE
                
                if event.key == pygame.K_ESCAPE:
                    self.main_menu = True

        return self.player_rect.rect.x + x, self.player_rect.rect.y + y, self.main_menu

    def update_player_position(self, new_x, new_y):
        if self.maze.level_data[new_y // TILE_SIZE][new_x // TILE_SIZE] != "X":
            self.player_rect.x = new_x
            self.player_rect.y = new_y

            if self.maze.level_data[new_y // TILE_SIZE][new_x // TILE_SIZE] == "S" and not self.on_s_block:
                self.game_state["level"] += 1
                self.on_s_block = True
                self.switch_level()
            elif self.maze.level_data[new_y // TILE_SIZE][new_x // TILE_SIZE] != "S":
                self.on_s_block = False

if __name__ == "__main__":
    game = Game()
    game.game_start()