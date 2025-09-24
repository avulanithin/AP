# 4. using tkinter Email Generator Inputs: Name, Domain (gmail.com, yahoo.com, outlook.com). Output: Full email address
import tkinter as tk
import random
import string

def generate_email():
    name = name_entry.get().strip()
    domain = domain_var.get()
    
    if not name:
        result_label.config(text="Please enter a valid name.")
        return
    
    # Generate a random number to append to the name for uniqueness
    random_number = ''.join(random.choices(string.digits, k=3))
    email = f"{name.lower()}{random_number}@{domain}"
    
    result_label.config(text=f"Generated Email: {email}")
root = tk.Tk()
root.title("Email Generator")

# Create and place the input fields and labels
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Domain:").grid(row=1, column=0)
domain_var = tk.StringVar(value="gmail.com")
domain_menu = tk.OptionMenu(root, domain_var, "gmail.com", "yahoo.com", "outlook.com")
domain_menu.grid(row=1, column=1)

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Email", command=generate_email)
generate_button.grid(row=2, columnspan=2)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

root.mainloop()