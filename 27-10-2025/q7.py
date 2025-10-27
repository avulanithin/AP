# Q7. Using PyGame, design a mini interactive window where:
# • A small circle moves using arrow keys.
# • Background color changes when the circle hits window borders.
# • The window closes on pressing the Escape key.
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Interactive Circle")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Circle properties
circle_pos = [width // 2, height // 2]
circle_radius = 20
circle_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_pos[0] -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_pos[0] += circle_speed
    if keys[pygame.K_UP]:
        circle_pos[1] -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_pos[1] += circle_speed

    # Check for collisions with window borders
    if circle_pos[0] - circle_radius < 0 or circle_pos[0] + circle_radius > width:
        screen.fill(random.choice([black, white, red]))
    if circle_pos[1] - circle_radius < 0 or circle_pos[1] + circle_radius > height:
        screen.fill(random.choice([black, white, red]))

    # Clear the screen
    screen.fill(white)

    # Draw the circle
    pygame.draw.circle(screen, red, circle_pos, circle_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
exit()
