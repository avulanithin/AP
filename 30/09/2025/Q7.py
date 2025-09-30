import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Moving Ball")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create a ball turtle
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(-350, 0)  # Start at the left side
ball_speed = 20  # Step size per movement

# Functions to move the ball
def move_up():
    y = ball.ycor()
    if y < 290:  # Stay inside top boundary
        ball.sety(y + ball_speed)

def move_down():
    y = ball.ycor()
    if y > -290:  # Stay inside bottom boundary
        ball.sety(y - ball_speed)

def move_left():
    x = ball.xcor()
    if x > -390:  # Stay inside left boundary
        ball.setx(x - ball_speed)

def move_right():
    x = ball.xcor()
    if x < 390:  # Stay inside right boundary
        ball.setx(x + ball_speed)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Keep window open
screen.mainloop()
