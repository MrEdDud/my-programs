import pygame, sys
from main_menu import main_menu
from quiz import run_quiz
from celebration import run_celebration
from config import clock
pygame.init()

# Game states
current_state = 1

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # State handling
    if current_state == 1:
        current_state = main_menu()
    elif current_state == 2:
        current_state = run_quiz()
    elif current_state == 3:
        current_state = run_celebration()

    clock.tick(60)
    pygame.display.update()