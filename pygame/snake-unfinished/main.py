import pygame, random
pygame.init()

def food_position():
    x = random.randint(0, (SCREEN_WIDTH - 50) // 50) * 50
    y = random.randint(0, (SCREEN_HEIGHT - 50) // 50) * 50
    return x, y

# Creating the caption of the game
pygame.display.set_caption("Snake")
# Creating the icon of the game
icon = pygame.image.load("graphics/icon.png")
pygame.display.set_icon(icon)

# Constants for holding the width and height of our display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Creating the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Declaring variables
clock = pygame.time.Clock()
food = 0
snake_length = 2
snake_segments = [(0, 300), (50, 300)]

# Creating the snake
snake_surf = pygame.Surface((50, 50))
snake_surf.fill((52, 78, 65))
#snake_rect = snake_surf.get_rect(topleft = (0,300))

# Creating the food
food_surf = pygame.Surface((50, 50))
food_surf.fill((111, 29, 27))
food_rect = food_surf.get_rect(topleft = food_position())

# Game loop
while True:
    screen.fill((163, 177, 138))
    # Checks for each event
    for event in pygame.event.get():
        # Checks if the event is the close button
        if event.type == pygame.QUIT:
            # Closes the game
            pygame.quit()
            exit()
        # Checks if a key has been pressed down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: # Checks if the 'a' key has been pressed
                snake_segments[0].left -= 50
            elif event.key == pygame.K_w: # Checks if the 'w' key has been pressed
                snake_segments[0].top -= 50
            elif event.key == pygame.K_s: # Checks if the 's' key has been pressed
                snake_segments[0].top += 50
            elif event.key == pygame.K_d: # Checks if the 'd' key has been pressed
                snake_segments[0].left += 50

    #snake_segments.append((snake_rect.left, snake_rect.top))

    if len(snake_segments) > snake_length:
        snake_segments.pop(0)

    for segment in snake_segments:
        screen.blit(snake_surf, segment)
    
    screen.blit(food_surf, food_rect)

    #food_collision = snake_rect.colliderect(food_rect)
    
    if snake_segments == food_rect.topleft:
        food_rect.topleft = food_position()
        food += 1
        snake_length += 1

    # Updates the display every time the game loops
    pygame.display.update()
    # Tells the while loop to not run more than 60 time per second
    clock.tick(60)