# Q9. Simple Sprite Game – Load an image (test.png), display it, and move it with arrow keys.
import tkinter as tk

# Create window
root = tk.Tk()
root.title("Sprite Game")
root.geometry("800x600")

# Create canvas
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Load player image (PNG supported)
player_img = tk.PhotoImage(file="test.png")
player = canvas.create_image(400, 300, image=player_img)

move_speed = 20

# Movement functions
def move_up(event):
    canvas.move(player, 0, -move_speed)

def move_down(event):
    canvas.move(player, 0, move_speed)

def move_left(event):
    canvas.move(player, -move_speed, 0)

def move_right(event):
    canvas.move(player, move_speed, 0)

# Bind arrow keys
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

root.mainloop()
