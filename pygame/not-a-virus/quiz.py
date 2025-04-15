import pygame, sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, small_font, font, screen, clock, icon, resource_path
pygame.init()

# Setup
background = pygame.image.load(resource_path("graphics/background.png"))
pygame.display.set_icon(icon)

x = 130
y = x*2

# Quiz images
image_1 = pygame.transform.scale(pygame.image.load(resource_path("graphics/quiz/1.png")), (y, x))
image_2 = pygame.transform.scale(pygame.image.load(resource_path("graphics/quiz/2.png")), (y, x))
image_3 = pygame.transform.scale(pygame.image.load(resource_path("graphics/quiz/3.png")), (y, x))
image_4 = pygame.transform.scale(pygame.image.load(resource_path("graphics/quiz/4.png")), (y, x))
image_5 = pygame.transform.scale(pygame.image.load(resource_path("graphics/quiz/5.png")), (y, x))
image_6 = pygame.transform.scale(pygame.image.load(resource_path("graphics/quiz/6.png")), (y, x))


# Sounds
correct = pygame.mixer.Sound(resource_path("sounds/correct.wav"))
yipee = pygame.mixer.Sound(resource_path("sounds/yipee.wav"))
mogging = pygame.mixer.Sound(resource_path("sounds/mogging.wav"))
aneurysm = pygame.mixer.Sound(resource_path("sounds/aneurysm.wav"))
out = pygame.mixer.Sound(resource_path("sounds/out.wav"))
retard_alert = pygame.mixer.Sound(resource_path("sounds/retard_alert.wav"))
retard = pygame.mixer.Sound(resource_path("sounds/retard.wav"))
violin = pygame.mixer.Sound(resource_path("sounds/violin.wav"))
vsauce = pygame.mixer.Sound(resource_path("sounds/vsauce.wav"))

# Buttons
button_height = 50
button_width = 260
button_vertical_spacing = 50
button_y_offset = 190
button1 = pygame.Rect(SCREEN_WIDTH // 3, button_y_offset, button_width, button_height)
button2 = pygame.Rect(SCREEN_WIDTH // 3, button_y_offset + button_height + button_vertical_spacing, button_width, button_height)
button3 = pygame.Rect(SCREEN_WIDTH // 3, button_y_offset + 2 * (button_height + button_vertical_spacing), button_width, button_height)

# Incorrect answer
big_x_font = pygame.font.Font(None, 1000)
big_x = big_x_font.render("X", True, (255, 0, 0))
big_x_rect = big_x.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 50))

# Questions
questions = [
    {
        'question': "Which picture is the best?",
        'options': [image_1, image_2, image_3],
        'sounds': [correct, out, violin],
        'correct': 0,
    },
    {
        'question': "Which picture is the best? again.",
        'options': [image_4, image_5, image_6],
        'sounds': [aneurysm, yipee, vsauce],
        'correct': 1,
    },
    {
        'question': "Which statement about Mr Eduard Cojocaru is true? you already know ;)",
        'options': ["1. he is the sexiest and most beautiful man alive", "2. hes dating your granddad", "3. he is the most ugly & miserable prick you have ever had the grace to encounter"],
        'sounds': [mogging, retard, retard_alert],
        'correct': 0,
    }
]

current_question = 0

# Text wrapping function
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        # Check the width of the line if we add the next word
        test_line = current_line + ' ' + word if current_line else word
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:  # If there's text in the line, add it to lines
                lines.append(current_line)
            current_line = word  # Start a new line with the current word

    if current_line:  # Add any remaining text as the last line
        lines.append(current_line)

    return lines

show_wrong = False
wrong_timer = 0
WRONG_TIME = 1500  

# Game loop 
def run_quiz():
    global current_question, show_wrong, wrong_timer, WRONG_TIME
    while True:
        screen.fill((30, 30, 30))
        screen.blit(background, (0,0))
        mouse_pos = pygame.mouse.get_pos()
        clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
        
        # Get current question
        question = questions[current_question]
        # Wrap question text
        max_width = SCREEN_WIDTH - 40  # Padding of 20px from left and right
        wrapped_text = wrap_text(question['question'], font, max_width)

        # Draw wrapped question text
        y_offset = 50  # Start drawing at y-position
        for line in wrapped_text:
            question_text = font.render(line, True, (255, 255, 255))
            question_rect = question_text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            screen.blit(question_text, question_rect)
            y_offset += question_text.get_height() + 5  # Move down for next line

        if current_question < 2:  # Image-based questions
            # Display images
            for i, img in enumerate(question['options']):
                img_rect = pygame.Rect((SCREEN_WIDTH // 3) * (i % 3), SCREEN_HEIGHT // 2 + (i // 3) * 60, 100, 100)
                screen.blit(img, img_rect.topleft)

                # Handle click on images
                if img_rect.collidepoint(mouse_pos) and clicked:
                    if i == question['correct']:
                        question['sounds'][i].play()
                        current_question += 1
                    else:
                        question['sounds'][i].play()
                        show_wrong = True
                        wrong_timer = pygame.time.get_ticks()

        else:  # Text-based question
            # Draw text buttons
            for i, option in enumerate(question['options']):
                button_text = small_font.render(option, True, (255, 255, 255))
                button_rect = button1 if i == 0 else button2 if i == 1 else button3
                pygame.draw.rect(screen, (60, 60, 60), button_rect, border_radius=10)
                button_text_rect = button_text.get_rect(center=button_rect.center)
                screen.blit(button_text, button_text_rect)

                if button_rect.collidepoint(mouse_pos) and clicked:
                    if i == question['correct']:
                        question['sounds'][i].play()
                        current_question += 1
                    else:
                        question['sounds'][i].play()
                        show_wrong = True
                        wrong_timer = pygame.time.get_ticks()  

        if show_wrong:
            screen.blit(big_x, big_x_rect)
            pygame.display.update()

            if pygame.time.get_ticks() - wrong_timer >= WRONG_TIME:
                show_wrong = False
        
        if current_question >= len(questions):
            return 3

        pygame.display.update()
        clock.tick(60)