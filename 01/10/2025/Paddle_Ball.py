# Mini Game 1: Paddle Ball (Mini Pong)
# - Create a paddle (rectangle) at the bottom of the screen.
# - A ball (circle) falls from the top.
# - Move the paddle left/right with arrow keys.
# - If the paddle catches the ball, increase score by 1.
# - If the ball touches the bottom, game over.

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paddle Ball (Mini Pong)")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CHARTREUSE = (127, 255, 0)
TOMATO = (255, 99, 71)
RED = (255, 0, 0)

# Paddle settings
paddle_width, paddle_height = 80, 12
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 40
paddle_speed = 6

# Ball settings
ball_radius = 10
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = 3

# Score
score = 0
game_over = False
font = pygame.font.SysFont("Arial", 20)

clock = pygame.time.Clock()

def draw_objects():
    screen.fill(BLACK)

    # Draw paddle
    pygame.draw.rect(screen, CHARTREUSE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(screen, TOMATO, (ball_x, ball_y), ball_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

# Main loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move paddle
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # Boundaries
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x + paddle_width > WIDTH:
        paddle_x = WIDTH - paddle_width

    if not game_over:
        # Move ball
        ball_y += ball_speed

        # Check catch
        if (ball_y + ball_radius >= paddle_y and
            paddle_x <= ball_x <= paddle_x + paddle_width):
            score += 1
            ball_x = random.randint(ball_radius, WIDTH - ball_radius)
            ball_y = 0
            ball_speed += 0.2  # increase difficulty

        # Missed ball
        if ball_y + ball_radius >= HEIGHT:
            game_over = True

    draw_objects()
