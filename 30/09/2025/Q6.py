# Q6. Color Switcher – Change the background color:
#- Red when R key is pressed
#- Green when G key is pressed
#- Blue when B key is pressed


import tkinter as tk

# Function to change background color
def change_color(event):
    key = event.keysym.upper()  # Get pressed key
    if key == "R":
        root.config(bg="red")
    elif key == "G":
        root.config(bg="green")
    elif key == "B":
        root.config(bg="blue")

# Create main window
root = tk.Tk()
root.title("Color Switcher")
root.geometry("400x300")
root.config(bg="white")  # Default color

# Bind key press
root.bind("<KeyPress>", change_color)

# Run the GUI loop
root.mainloop()
