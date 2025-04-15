import pygame, json, time # Importing different modules
pygame.init() # Initialising Pygame

pygame.display.set_caption("Maze Game") # Setting the game name

SCREEN_WIDTH = 750 # Setting the screen width
SCREEN_HEIGHT = 450 # Setting the screen height
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creating the display

large_font = pygame.font.SysFont('Consolas', 54, bold=True) # Setting the font
font = pygame.font.SysFont('Consolas', 36) # Setting the font
small_font = pygame.font.SysFont('Consolas', 22) # Setting the font

clock = pygame.time.Clock() # Initialising the clock
TILE_SIZE = 50 # Setting the tile size
on_s_block = False
main_menu = True

background_image = pygame.image.load("image.png")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Dictionary storing values of the player to save
game_state = {
    "level": 0
}

# The mazes
level_1 = [
    "XXXXXXXXXXXXXXX",
    "X           X X",
    "X XXXXX XXXXX X",
    "X X      X    X",
    "X X XXXXXX XX X",
    "X X X       X X",
    "X   X XXXXX X X",
    "XXX         XSX",
    "XXXXXXXXXXXXXXX"
]

level_2 = [
    "XXXXXXXXXXXXXXX",
    "X  X          X",
    "X XXXXX XXXXX X",
    "X X      X    X",
    "X X XXXXXX XX X",
    "X X X       XXX",
    "X   X XXXXX   X",
    "X X XS      X X",
    "XXXXXXXXXXXXXXX"
]
# Function to save the game
def save_game_state(filename):
    with open(filename, "w") as f:
        json.dump(game_state, f)
# Function to load the game
def load_game_state(filename):
    with open(filename, "r") as f:
        loaded_state = json.load(f)
        game_state.update(loaded_state)

player_rect = pygame.Rect((TILE_SIZE, TILE_SIZE, TILE_SIZE, TILE_SIZE))  # Creating a player rectangle

# Function to draw the player
def draw_player(x):
    pygame.draw.rect(screen, (214, 40, 40), x)  # Drawing the player
# Function to draw the maze
def draw_maze():
    for row_num, row in enumerate(level_1):
        for column_num, tile_type in enumerate(row):
            x = column_num * TILE_SIZE
            y = row_num * TILE_SIZE
            colours = {
                "X": (96, 108, 56),
                "S": (188, 108, 37)
            }.get(tile_type, (254, 250, 224))
            pygame.draw.rect(screen, colours, (x, y, TILE_SIZE, TILE_SIZE))
    draw_player(player_rect)

# Function for the main menu
def main_menu_screen():
    global main_menu
    colours = ["White", "Gray"]
    play_x, options_x, quit_x = 0, 0, 0
    while main_menu:
        for event in pygame.event.get():
            # Checks if the player has quit the program
            if event.type == pygame.QUIT:
                save_game_state("savegame.json") # Saves the game
                pygame.quit()
                exit()
            # Checks if the user has pressed space or enter to return to the game
            """if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    main_menu = False"""
            """# Changes button colours if they have been hovered over
            if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    if play_text_rect.collidepoint(mouse_pos): 
                        play_x = 1
                    else: 
                        play_x = 0
                    
                    if options_text_rect.collidepoint(mouse_pos): 
                        options_x = 1
                    else: 
                        options_x = 0
                    
                    if quit_text_rect.collidepoint(mouse_pos): 
                        quit_x = 1
                    else: 
                        quit_x = 0"""
            # Adds functionality to the buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_text_rect.collidepoint(mouse_pos): # Play button
                    main_menu = False
                if options_text_rect.collidepoint(mouse_pos): # Options button
                    pass
                if quit_text_rect.collidepoint(mouse_pos): # Quit button
                    save_game_state("savegame.json") # Saves the game
                    pygame.quit()
                    exit()
            
        #screen.blit(background_image, background_image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))

        # Game name
        name_text_surface = large_font.render("Maze Game", True, colours[0])
        name_text_rect = name_text_surface.get_rect(center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-150))
        screen.blit(name_text_surface, name_text_rect)

        # Play button
        play_text_surface = font.render("Begin", True, colours[play_x])
        play_text_rect = play_text_surface.get_rect(center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-50))
        screen.blit(play_text_surface, play_text_rect)

        # Options button
        options_text_surface = font.render("Options", True, colours[options_x])
        options_text_rect = options_text_surface.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(options_text_surface, options_text_rect)
        
        # Quit button
        quit_text_surface = font.render("Quit", True, colours[quit_x])
        quit_text_rect = quit_text_surface.get_rect(center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)+50))
        screen.blit(quit_text_surface, quit_text_rect)

        # Text
        info_text_surface = small_font.render("Press Enter to start!", True, colours[0])
        info_text_rect = info_text_surface.get_rect(center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)+150))
        screen.blit(info_text_surface, info_text_rect)

        pygame.display.update() # Updating the display
        clock.tick(60) # Setting the max FPS to 60

def switch_level():
    global player_rect, level_1, level_2
    if game_state["level"] == 1:
        player_rect.x = TILE_SIZE
        player_rect.y = TILE_SIZE
        level_1 = level_2

load_game_state("savegame.json") # Loads the game

# Game loop
while True:
    x, y = 0, 0
    for event in pygame.event.get():
        # Checks if the player has quit the program
        if event.type == pygame.QUIT:
            save_game_state("savegame.json") # Saves the game
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
                main_menu = True

    new_x, new_y = player_rect.x + x, player_rect.y + y

    if main_menu == True:
        main_menu_screen()

    if level_1[new_y // TILE_SIZE][new_x // TILE_SIZE] != "X":
        player_rect.x = new_x
        player_rect.y = new_y

        if level_1[new_y // TILE_SIZE][new_x // TILE_SIZE] == "S" and not on_s_block:
            game_state["level"] += 1
            on_s_block = True
            switch_level()
        elif level_1[new_y // TILE_SIZE][new_x // TILE_SIZE] != "S":
            on_s_block = False
    
    draw_maze() # Drawing the maze

    pygame.display.update() # Updating the display
    clock.tick(60) # Setting the max FPS to 60