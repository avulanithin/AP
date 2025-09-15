"""Simple Calculator with Tkinter GUI (PEP8 Compliant)."""

import tkinter as tk
from tkinter import messagebox


class Calculator(tk.Tk):
    """A simple calculator app using Tkinter."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x400")
        self.resizable(True, True)

        self.expression = ""
        self.input_text = tk.StringVar()

        self._create_ui()

    def _create_ui(self) -> None:
        """Create calculator UI elements."""
        input_frame = tk.Frame(self, bd=2, relief=tk.RIDGE)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        input_field = tk.Entry(
            input_frame,
            font=("Arial", 18),
            textvariable=self.input_text,
            justify="right",
            bd=5,
        )
        input_field.pack(fill=tk.BOTH, ipadx=8, ipady=8)

        button_frame = tk.Frame(self, bg="lightgrey")
        button_frame.pack(fill=tk.BOTH, expand=True)

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
            ("C", 5, 0, 4),
        ]

        for text, row, col, *span in buttons:
            colspan = span[0] if span else 1
            btn = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 14),
                height=2,
                width=6 if colspan == 1 else 28,
                command=lambda t=text: self._on_button_click(t),
            )
            btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2)

    def _on_button_click(self, char: str) -> None:
        """Handle button click events."""
        if char == "=":
            self._calculate()
        elif char == "C":
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def _calculate(self) -> None:
        """Evaluate the current expression."""
        try:
            result = str(eval(self.expression))  # safe here since input is button-based
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            self.input_text.set("")
            self.expression = ""
        except Exception:
            messagebox.showerror("Error", "Invalid Expression.")
            self.input_text.set("")
            self.expression = ""


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
