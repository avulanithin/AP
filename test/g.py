import pygame
pygame.init()

# Window setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Moving Ball")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Ball properties
x = 300
y = 200
radius = 20
speed = 1

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Fill screen and draw ball
    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), radius)
    pygame.display.update()

pygame.quit()
