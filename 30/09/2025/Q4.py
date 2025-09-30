# Q4. Keyboard Event – Print &#39;UP Arrow Pressed&#39; when UP key is pressed and &#39;DOWN Arrow Released&#39; when DOWN key is released.
import tkinter as tk

# Function when UP key is pressed
def on_key_press(event):
    if event.keysym == "Up":
        print("UP Arrow Pressed")

# Function when DOWN key is released
def on_key_release(event):
    if event.keysym == "Down":
        print("DOWN Arrow Released")

# Create main window
root = tk.Tk()
root.title("Keyboard Event Example")
root.geometry("300x200")

# Bind events
root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)

# Run the GUI loop
root.mainloop()
