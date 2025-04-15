import pygame, random
# Function for the ball animation
def ball_animation():
    global ball_speed_x, ball_speed_y
    # Animation for the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Making the borders for the ball
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_restart()
    # Changes ball direction when collision with player/opponent
    if player.colliderect(ball) or opponent.colliderect(ball):
        ball_speed_x *= -1
# Function for the player's animations
def players_animation():
    global player_moving_up, player_moving_down, opponent_moving_up, opponent_moving_down
    # Player movement
    if player_moving_up:
        player.y -= platform_speed
    elif player_moving_down:
        player.y += platform_speed
    # Opponent movement
    if opponent_moving_up:
        opponent.y -= platform_speed
    elif opponent_moving_down:
        opponent.y += platform_speed
    # Stops player/opponent from leaving the screen
    if player.top <= 0 or player.bottom >= SCREEN_HEIGHT:
        player_moving_up, player_moving_down = 0, 0
    if opponent.top <= 0 or opponent.bottom >= SCREEN_HEIGHT:
        opponent_moving_up, opponent_moving_down = 0, 0
# Function for the ball after hitting one of the walls
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Game rectangles
ball = pygame.Rect(SCREEN_WIDTH / 2 - 15, SCREEN_HEIGHT / 2 - 15, 30, 30)
player = pygame.Rect(10, SCREEN_HEIGHT / 2 - 70, 10, 140)
opponent = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - 70, 10, 140)

# Animation speed
platform_speed = 7
ball_speed_x = 7
ball_speed_y = 7

# Storing when the player's are moving up/down
player_moving_up = False
player_moving_down = False
opponent_moving_up = False
opponent_moving_down = False

# Game loop
while True:
    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_moving_up = True
            elif event.key == pygame.K_s:
                player_moving_down = True
            elif event.key == pygame.K_UP:
                opponent_moving_up = True
            elif event.key == pygame.K_DOWN:
                opponent_moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_moving_up = False
            elif event.key == pygame.K_s:
                player_moving_down = False
            elif event.key == pygame.K_UP:
                opponent_moving_up = False
            elif event.key == pygame.K_DOWN:
                opponent_moving_down = False
    
    # Calling functions
    ball_animation()
    players_animation()

    # Visuals
    screen.fill((206, 212, 218))
    pygame.draw.rect(screen, ((33, 37, 41)), player)
    pygame.draw.rect(screen, ((33, 37, 41)), opponent)
    pygame.draw.aaline(screen, (33, 37, 41), (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))
    pygame.draw.ellipse(screen, ((33, 37, 41)), ball)

    # Updating the window
    pygame.display.update()
    clock.tick(60)