import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Bouncing Ball")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)

# Ball speed
dx = 5  # Change in x
dy = 3  # Change in y

# Main animation loop
while True:
    # Move the ball
    x = ball.xcor() + dx
    y = ball.ycor() + dy
    ball.goto(x, y)

    # Check for collision with window edges
    if x > 390 or x < -390:
        dx = -dx  # Reverse horizontal direction
    if y > 290 or y < -290:
        dy = -dy  # Reverse vertical direction

    screen.update()  # Update the screen
