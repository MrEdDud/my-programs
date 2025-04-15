import pygame

class Maze:
    def __init__(self, TILE_SIZE, screen):
        self.tile_size = TILE_SIZE
        self.screen = screen
        self.level_data = []
        self.load_level(1)

    def load_level(self, level):
        if level == 1:
            self.level_data = [
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
        elif level == 2:
            self.level_data = [
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
    
    # Function to draw the maze
    def draw_maze(self):
        for row_num, row in enumerate(self.level_data):
            for column_num, tile_type in enumerate(row):
                x = column_num * self.tile_size
                y = row_num * self.tile_size
                colours = {
                    "X": (96, 108, 56),
                    "S": (188, 108, 37)
                }.get(tile_type, (254, 250, 224))
                pygame.draw.rect(self.screen, colours, (x, y, self.tile_size, self.tile_size))
