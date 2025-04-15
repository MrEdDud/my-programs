import pygame, os, sys
pygame.init()

# Helper function
def resource_path(relative_path):
    """ Get the absolute path to a resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setup
menu_caption = "NOT A VIRUS, i pwomise :)))"
icon = pygame.image.load(resource_path("graphics/icon.png"))
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 30)