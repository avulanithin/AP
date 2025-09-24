# Build a Simple Calculator  with Tkinter 2 entry fields for numbers 4 buttons (+, -, ×, ÷) Label to show result
import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry1 = tk.Entry(master)
        self.entry1.grid(row=0, column=0)

        self.entry2 = tk.Entry(master)
        self.entry2.grid(row=0, column=1)

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.grid(row=1, column=0, columnspan=2)

        self.add_button = tk.Button(master, text="+", command=self.add)
        self.add_button.grid(row=2, column=0)

        self.subtract_button = tk.Button(master, text="-", command=self.subtract)
        self.subtract_button.grid(row=2, column=1)

        self.multiply_button = tk.Button(master, text="×", command=self.multiply)
        self.multiply_button.grid(row=2, column=2)

        self.divide_button = tk.Button(master, text="÷", command=self.divide)
        self.divide_button.grid(row=2, column=3)

    def add(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        result = num1 + num2
        self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        result = num1 - num2
        self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        result = num1 * num2
        self.result_label.config(text=f"Result: {result}")

    def divide(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        if num2 != 0:
            result = num1 / num2
            self.result_label.config(text=f"Result: {result}")
        else:
            messagebox.showerror("Error", "Division by zero is not allowed.")

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
