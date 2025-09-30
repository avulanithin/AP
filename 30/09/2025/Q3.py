# Q3. Shapes Drawing – Draw: - A red rectangle (100×50) - A green circle (radius 40) - A black line across the screen




import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Shapes Drawing")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(3)

# 1. Draw a red rectangle (100 × 50)
pen.color("red", "red")  # outline + fill color
pen.begin_fill()
for _ in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
pen.end_fill()

# Move to new position for circle
pen.penup()
pen.goto(150, 0)
pen.pendown()

# 2. Draw a green circle (radius 40)
pen.color("green", "green")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

# 3. Draw a black line across the screen
pen.penup()
pen.goto(-200, -100)
pen.pendown()
pen.color("black")
pen.forward(400)

# Finish
turtle.done()
