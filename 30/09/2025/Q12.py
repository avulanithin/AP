import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Group Project Game")

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Background color
bg_color = BLUE

# Clock
clock = pygame.time.Clock()

# Moving ball
ball_radius = 20
ball_x, ball_y = 50, HEIGHT//2
ball_speed = 5

# Bouncing ball
bball_radius = 20
bball_x, bball_y = WIDTH//2, HEIGHT//2
bball_dx, bball_dy = 4, 3

# Player sprite
player_img = pygame.image.load("test.png")
player_rect = player_img.get_rect()
player_rect.topleft = (WIDTH//2, HEIGHT-100)
player_speed = 5

# Score for circle catch
score = 0

# Circle for mouse click
click_circles = []

# Main loop
running = True
while running:
    screen.fill(bg_color)
    
    # Draw shapes
    pygame.draw.rect(screen, RED, (50, 50, 100, 50))           # Red rectangle
    pygame.draw.circle(screen, GREEN, (200, 100), 40)          # Green circle
    pygame.draw.line(screen, BLACK, (0, 150), (WIDTH, 150), 3)# Black line

    # Draw moving ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw bouncing ball
    pygame.draw.circle(screen, GREEN, (bball_x, bball_y), bball_radius)

    # Draw player sprite
    screen.blit(player_img, player_rect)

    # Draw mouse click circles
    for pos in click_circles:
        pygame.draw.circle(screen, WHITE, pos, 15)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Keyboard events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP Arrow Pressed")
            elif event.key == pygame.K_r:
                bg_color = RED
            elif event.key == pygame.K_g:
                bg_color = GREEN
            elif event.key == pygame.K_b:
                bg_color = BLUE
            elif event.key == pygame.K_SPACE:
                beep_sound = pygame.mixer.Sound("beep.wav")
                beep_sound.play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                print("DOWN Arrow Released")
        
        # Mouse click event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_circles.append(event.pos)
    
    # Continuous keyboard state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_x += ball_speed
    if keys[pygame.K_UP]:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_y += ball_speed

    # Player sprite movement
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_d]:
        player_rect.x += player_speed
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_s]:
        player_rect.y += player_speed

    # Keep ball inside screen
    ball_x = max(ball_radius, min(WIDTH-ball_radius, ball_x))
    ball_y = max(ball_radius, min(HEIGHT-ball_radius, ball_y))

    # Bouncing ball movement
    bball_x += bball_dx
    bball_y += bball_dy
    if bball_x - bball_radius < 0 or bball_x + bball_radius > WIDTH:
        bball_dx = -bball_dx
    if bball_y - bball_radius < 0 or bball_y + bball_radius > HEIGHT:
        bball_dy = -bball_dy

    # Update screen
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
