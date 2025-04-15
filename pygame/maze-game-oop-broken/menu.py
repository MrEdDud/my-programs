import pygame, json

class Menu:
    def __init__(self, screen, fonts, clock, TILE_SIZE, game_state, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.screen = screen
        self.font = fonts
        self.clock = clock
        self.tile_size = TILE_SIZE
        self.game_state = game_state
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.colours = ["White", "Gray"]

    def main_menu_screen(self):
        main_menu = True
        x = 0
        while main_menu:
            for event in pygame.event.get():
                # Checks if the player has quit the program
                if event.type == pygame.QUIT:
                    self.save_game_state("savegame.json") # Saves the game
                    pygame.quit()
                    exit()
                # Checks if the user has pressed space or enter to return to the game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        main_menu = False
                
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    text_surface = self.font.render("Play", True, self.colours[0])
                    text_rect = text_surface.get_rect(center = (self.screen_width/2, self.screen_height/2))
                    if text_rect.collidepoint(mouse_pos): 
                        x = 1
                    else: 
                        x = 0
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if text_rect.collidepoint(mouse_pos):
                        main_menu = False

            self.screen.fill("Black")
            text_surface = self.font.render("Play", True, self.colours[x])
            text_rect = text_surface.get_rect(center = (self.screen_width/2, self.screen_height/2))
            self.screen.blit(text_surface, text_rect)
            
            pygame.display.update() # Updating the display
            self.clock.tick(60) # Setting the max FPS to 60
    
    def save_game_state(self, filename):
        with open(filename, "w") as f:
            json.dump(self.game_state, f)
