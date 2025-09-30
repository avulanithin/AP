import tkinter as tk
import random

# Window setup
WIDTH, HEIGHT = 800, 600
root = tk.Tk()
root.title("Catch the Circle")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Player rectangle
player_size = 50
player = canvas.create_rectangle(0, 0, player_size, player_size, fill="blue")
canvas.move(player, WIDTH//2, HEIGHT - player_size - 10)  # Start at bottom center

# Circle
circle_radius = 20
circle = canvas.create_oval(0, 0, circle_radius*2, circle_radius*2, fill="red")

# Score
score = 0
score_text = canvas.create_text(70, 30, text=f"Score: {score}", font=("Arial", 20), fill="black")

# Movement speed
move_speed = 20

# Function to move player
def move_up(event):
    if canvas.coords(player)[1] > 0:
        canvas.move(player, 0, -move_speed)

def move_down(event):
    if canvas.coords(player)[3] < HEIGHT:
        canvas.move(player, 0, move_speed)

def move_left(event):
    if canvas.coords(player)[0] > 0:
        canvas.move(player, -move_speed, 0)

def move_right(event):
    if canvas.coords(player)[2] < WIDTH:
        canvas.move(player, move_speed, 0)

# Bind keys
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Function to place circle at random position
def move_circle():
    x = random.randint(0, WIDTH - circle_radius*2)
    y = random.randint(0, HEIGHT - circle_radius*2)
    canvas.coords(circle, x, y, x + circle_radius*2, y + circle_radius*2)

# Collision detection
def check_collision():
    global score
    px1, py1, px2, py2 = canvas.coords(player)
    cx1, cy1, cx2, cy2 = canvas.coords(circle)
    
    # Check if rectangle intersects circle
    if px2 > cx1 and px1 < cx2 and py2 > cy1 and py1 < cy2:
        score += 1
        canvas.itemconfig(score_text, text=f"Score: {score}")
        move_circle()  # Move circle to new position
    
    root.after(50, check_collision)  # Repeat collision check

# Initialize game
move_circle()
check_collision()

root.mainloop()
