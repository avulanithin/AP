# Simple Photo Editor (Tkinter + Pillow)
# Features:
# 1) Choose image via File Dialog
# 2) Grayscale, Resize to 200x200, Blur
# 3) Display the processed image in a Label using PhotoImage

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter

# --- Global state to keep references ---
current_image = None      # Holds the current PIL.Image object
current_photo = None      # Holds the ImageTk.PhotoImage (must keep a reference to display in Tkinter)

def update_display(img):
    """Update the Label to show the given PIL image."""
    global current_image, current_photo
    current_image = img                      # save PIL image
    current_photo = ImageTk.PhotoImage(img)  # convert to PhotoImage (Tk compatible)
    img_label.config(image=current_photo)    # set label image
    img_label.image = current_photo          # extra ref (prevents garbage collection)

def open_image():
    """Open an image file and display it."""
    path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", ".png;.jpg;.jpeg;.bmp;*.gif")]
    )
    if not path:
        return  # user cancelled
    try:
        img = Image.open(path)          # open with Pillow
        img = img.convert("RGB")        # normalize mode for consistent processing/display
        update_display(img)             # show it
        set_buttons_state("normal")     # enable operation buttons
    except Exception as e:
        messagebox.showerror("Error", f"Could not open image:\n{e}")

def to_grayscale():
    """Convert current image to grayscale and display it."""
    if current_image is None:
        return
    gray = current_image.convert("L")   # convert to 8-bit grayscale
    update_display(gray)

def resize_200():
    """Resize current image to 200x200 and display it."""
    if current_image is None:
        return
    resized = current_image.resize((200, 200), Image.LANCZOS)
    update_display(resized)

def blur_image():
    """Apply a simple blur filter and display it."""
    if current_image is None:
        return
    blurred = current_image.filter(ImageFilter.BLUR)
    update_display(blurred)

def set_buttons_state(state):
    """Enable/disable operation buttons together."""
    btn_gray.config(state=state)
    btn_resize.config(state=state)
    btn_blur.config(state=state)

# --- Build the GUI ---
root = tk.Tk()
root.title("Mini Photo Editor")
root.geometry("500x450")

# Top: control buttons
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

btn_open = tk.Button(top_frame, text="Open Image", command=open_image)
btn_open.grid(row=0, column=0, padx=5)

btn_gray = tk.Button(top_frame, text="Grayscale", command=to_grayscale, state="disabled")
btn_gray.grid(row=0, column=1, padx=5)

btn_resize = tk.Button(top_frame, text="Resize 200×200", command=resize_200, state="disabled")
btn_resize.grid(row=0, column=2, padx=5)

btn_blur = tk.Button(top_frame, text="Blur", command=blur_image, state="disabled")
btn_blur.grid(row=0, column=3, padx=5)

# Center: image display area (Label with PhotoImage)
img_label = tk.Label(root, text="Open an image to begin", bd=1, relief="sunken", width=60, height=20)
img_label.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()