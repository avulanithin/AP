# Q5. Develop a Tkinter GUI that:
# • Allows users to enter their name and age.
# • Displays a greeting message when a button is clicked.
# • Includes a ‘Clear’ button to reset the inputs.
import tkinter as tk
from tkinter import messagebox

def greet():
    name = name_entry.get()
    age = age_entry.get()
    if name and age:
        messagebox.showinfo("Greeting", f"Hello {name}, you are {age} years old!")
    else:
        messagebox.showwarning("Input Error", "Please enter both your name and age.")
def clear():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create and place labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place buttons
greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()

