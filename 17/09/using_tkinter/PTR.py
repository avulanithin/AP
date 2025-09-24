# 5. Compound Interest Calculator Inputs: Principal, Rate, Time, Compounds per Year. Output: Final Amount using formula A = P(1+R/n)^(nT).
import tkinter as tk
from tkinter import messagebox

def calculate_compound_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get()) / 100
        time = float(time_entry.get())
        compounds_per_year = int(compounds_entry.get())

        # Calculate compound interest
        amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
        result_label.config(text=f"Final Amount: {amount:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Compound Interest Calculator")

# Create and place the input fields and labels
tk.Label(root, text="Principal:").grid(row=0, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

tk.Label(root, text="Rate (%):").grid(row=1, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1)

tk.Label(root, text="Time (years):").grid(row=2, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1)

tk.Label(root, text="Compounds per Year:").grid(row=3, column=0)
compounds_entry = tk.Entry(root)
compounds_entry.grid(row=3, column=1)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_compound_interest)
calculate_button.grid(row=4, columnspan=2)

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, columnspan=2)

root.mainloop()
