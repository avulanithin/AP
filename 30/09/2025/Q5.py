# Mouse Event – When the mouse is clicked, draw a circle at the clicked position.
import tkinter as tk
from PIL import Image, ImageTk

def draw_circle(event):
    x = event.x
    y = event.y
    radius = 20
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")

root = tk.Tk()
root.title("Mouse Event Example")
root.geometry("800x600")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<Button-1>", draw_circle)

root.mainloop()
