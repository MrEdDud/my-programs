import pygame, sys, math
from config import SCREEN_WIDTH, SCREEN_HEIGHT, small_font, font, screen, clock, icon, resource_path
from quiz import correct, yipee, mogging, aneurysm, out, retard_alert, retard, violin, vsauce
pygame.init()
pygame.mixer.set_num_channels(99999)

# Setup
background = pygame.transform.scale(pygame.image.load(resource_path("graphics/background_2.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_icon(icon)

# Buttons
celebration_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 60)

# Sounds
all_sounds = [correct, yipee, mogging, aneurysm, out, retard_alert, retard, violin, vsauce]

def get_rainbow_color(t):
    r = int(255 * (math.sin(t + 0) * 0.5 + 0.5))
    g = int(255 * (math.sin(t + 2 * math.pi / 3) * 0.5 + 0.5))
    b = int(255 * (math.sin(t + 4 * math.pi / 3) * 0.5 + 0.5))
    return r, g, b
t = 0

def run_celebration():
    while True:
        global t
        mouse_pos = pygame.mouse.get_pos()
        clicked = False

        screen.blit(background, (0,0))
        color = get_rainbow_color(t)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        message = font.render("HAPPY BIRTHDAY BITCH", True, color)
        message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(message, message_rect)

        t += 0.05

        pygame.draw.rect(screen, (30, 30, 30), celebration_button, border_radius=15)
        button_text = small_font.render("TOUCH ME ;)", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=celebration_button.center)
        screen.blit(button_text, button_rect)

        if celebration_button.collidepoint(mouse_pos) and clicked:
            for sound in all_sounds:
                channel = pygame.mixer.find_channel()
                if channel:
                    channel.play(sound)

        pygame.display.update()
        clock.tick(60)