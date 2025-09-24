# make a tkinter window that takes the first name and last name as input and has a button that shows a message box with the full name when clicked
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Name Input")

first_name_label = tk.Label(root, text="First Name:")
first_name_label.pack()

first_name_entry = tk.Entry(root)
first_name_entry.pack()

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.pack()

last_name_entry = tk.Entry(root)
last_name_entry.pack()

def show_full_name():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    full_name = f"{first_name} {last_name}"
    messagebox.showinfo("Full Name", full_name)

submit_button = tk.Button(root, text="Submit", command=show_full_name)
submit_button.pack()

root.mainloop()