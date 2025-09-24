# 2. using tkinter create Currency Converter Inputs: Amount, From Currency (INR/USD/EUR), To Currency (INR/USD/EUR). Output the converted value (use fixed rates).
import tkinter as tk
from tkinter import messagebox

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency == to_currency:
            result_label.config(text="Result: " + str(amount))
            return

        # Fixed conversion rates
        rates = {
            ("INR", "USD"): 0.013,
            ("USD", "INR"): 76.92,
            ("INR", "EUR"): 0.011,
            ("EUR", "INR"): 88.79,
            ("USD", "EUR"): 0.84,
            ("EUR", "USD"): 1.19
        }

        conversion_rate = rates.get((from_currency, to_currency))
        if not conversion_rate:
            raise ValueError("Invalid currency conversion.")

        converted_amount = amount * conversion_rate
        result_label.config(text=f"Result: {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

root = tk.Tk()
root.title("Currency Converter")

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

from_currency_var = tk.StringVar(value="INR")
to_currency_var = tk.StringVar(value="USD")

from_currency_menu = tk.OptionMenu(root, from_currency_var, "INR", "USD", "EUR")
from_currency_menu.grid(row=1, column=0)

to_currency_menu = tk.OptionMenu(root, to_currency_var, "INR", "USD", "EUR")
to_currency_menu.grid(row=1, column=1)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=2, column=0, columnspan=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
