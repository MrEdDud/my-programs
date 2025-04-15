import pygame, webbrowser, time, sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, small_font, font, screen, clock, menu_caption, icon, resource_path
pygame.init()

# Setup
background = pygame.image.load(resource_path("graphics/background.png"))
pygame.display.set_caption(menu_caption)
pygame.display.set_icon(icon)

# Icons
yt_icon = pygame.transform.scale(pygame.image.load(resource_path("graphics/youtube.png")), (40, 40))
tw_icon = pygame.transform.scale(pygame.image.load(resource_path("graphics/twitter.png")), (40, 40))
in_icon = pygame.transform.scale(pygame.image.load(resource_path("graphics/instagram.png")), (40, 40))

# Button rectangles
title_button_rect = pygame.Rect(SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 - 50, 300, 100)
yt_rect = pygame.Rect(20, SCREEN_HEIGHT - 60, 40, 40)
tw_rect = pygame.Rect(70, SCREEN_HEIGHT - 60, 40, 40)
in_rect = pygame.Rect(120, SCREEN_HEIGHT - 60, 40, 40)

# Donate button
donate_text = small_font.render("Donate", True, (255, 255, 255))
donate_rect = pygame.Rect(SCREEN_WIDTH - 110, SCREEN_HEIGHT - 50, 90, 30)

# Colors
GRAY = (30, 30, 30)
HIGHLIGHT = (100, 100, 100)
POPUP_COLOR = (30, 30, 30)
POPUP_TEXT_COLOR = (255, 255, 255)

# Opens urls
def open_url(url):
    webbrowser.open(url)

# Draws buttons
def draw_button(rect, text=None, color=GRAY, text_color=(255, 255, 255), font_obj=font):
    pygame.draw.rect(screen, color, rect, border_radius=10)
    if text:
        rendered = font_obj.render(text, True, text_color)
        text_rect = rendered.get_rect(center=rect.center)
        screen.blit(rendered, text_rect)

# Draws popups
def draw_popup(message):
    popup_rect = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, SCREEN_WIDTH // 2, 200)
    pygame.draw.rect(screen, POPUP_COLOR, popup_rect)
    
    title_text = small_font.render(message, True, POPUP_TEXT_COLOR)
    text_rect = title_text.get_rect(center=popup_rect.center)
    screen.blit(title_text, text_rect)

popup_active = False
popup_message = "fuckin hell man im not that broke"

def main_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        clicked = False

        screen.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

        title_text = font.render("NOT A VIRUS!11!!1!", True, (255, 0, 0))
        title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(title_text, title_text_rect)

        # CLICK ME button
        if title_button_rect.collidepoint(mouse_pos):
            draw_button(title_button_rect, "CLICK ME", HIGHLIGHT)
            if clicked:
                return 2
        else:
            draw_button(title_button_rect, "CLICK ME")

        # Social icons
        screen.blit(yt_icon, yt_rect.topleft)
        screen.blit(tw_icon, tw_rect.topleft)
        screen.blit(in_icon, in_rect.topleft)

        if yt_rect.collidepoint(mouse_pos) and clicked:
            open_url("https://www.youtube.com/watch?v=xvFZjo5PgG0")
        if tw_rect.collidepoint(mouse_pos) and clicked:
            open_url("https://www.youtube.com/watch?v=QkWq0rk-IEQ")
        if in_rect.collidepoint(mouse_pos) and clicked:
            open_url("https://www.youtube.com/watch?v=k6Or1Y_cNHE")

        # Donate button
        pygame.draw.rect(screen, GRAY, donate_rect, border_radius=8)
        donate_text_rect = donate_text.get_rect(center=donate_rect.center)
        screen.blit(donate_text, donate_text_rect)

        if donate_rect.collidepoint(mouse_pos) and clicked:
            popup_active = True
            draw_popup(popup_message)
            pygame.display.update()
            time.sleep(3)
            popup_active = False

        pygame.display.update()
        clock.tick(60)