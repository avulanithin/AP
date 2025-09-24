# 1. Create a tkinter app where the user enters marks in 5 subjects. Output the total and percentage. Validate marks between 0–100.
import tkinter as tk
from tkinter import messagebox

def calculate_marks():
    try:
        marks = [float(entry.get()) for entry in entries]
        if any(mark < 0 or mark > 100 for mark in marks):
            raise ValueError("Marks should be between 0 and 100.")
        
        total = sum(marks)
        percentage = (total / 500) * 100
        
        result_label.config(text=f"Total: {total}, Percentage: {percentage:.2f}%")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))


root = tk.Tk()
root.title("Marks Calculator")

entries = []
for i in range(5):
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

tk.Label(root, text="Subject 1").grid(row=0, column=0)
tk.Label(root, text="Subject 2").grid(row=1, column=0)
tk.Label(root, text="Subject 3").grid(row=2, column=0)
tk.Label(root, text="Subject 4").grid(row=3, column=0)
tk.Label(root, text="Subject 5").grid(row=4, column=0)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

calculate_button = tk.Button(root, text="Calculate", command=calculate_marks)
calculate_button.grid(row=6, column=0, columnspan=2)

root.mainloop()
