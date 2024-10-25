import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
TARGET_COLOR = (255, 0, 0)
TARGET_RADIUS = 30
FONT_COLOR = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicking Game")

# Font
font = pygame.font.Font(None, 36)

# Game variables
score = 0
target_position = (random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS), 
                   random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = ((mouse_x - target_position[0]) ** 2 + (mouse_y - target_position[1]) ** 2) ** 0.5
            if distance < TARGET_RADIUS:
                score += 1
                target_position = (random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS),
                                   random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS))

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the target
    pygame.draw.circle(screen, TARGET_COLOR, target_position, TARGET_RADIUS)

    # Render the score
    score_text = font.render(f'Score: {score}', True, FONT_COLOR)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()