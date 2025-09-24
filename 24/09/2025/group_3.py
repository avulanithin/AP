import tkinter as tk
from tkinter import messagebox

def register():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()

    # Validation checks
    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return
    
    age = int(age)
    if age < 18:
        messagebox.showerror("Error", "Age must be 18 or above.")
        return
    
    if "@" not in email:
        messagebox.showerror("Error", "Invalid email address.")
        return

    # Success
    lbl_result.config(text=f"Welcome {name}, your registration is successful!")

# GUI Window
root = tk.Tk()
root.title("Registration Form")
root.geometry("350x250")

# Labels and Entries
tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Age:").pack(pady=5)
entry_age = tk.Entry(root, width=30)
entry_age.pack()

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack()

# Submit Button
tk.Button(root, text="Register", command=register).pack(pady=10)

# Result Label
lbl_result = tk.Label(root, text="", fg="green")
lbl_result.pack(pady=10)

root.mainloop()