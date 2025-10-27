# Q6. Create a simple Tkinter Text Editor that:
# • Lets the user type text inside a textbox.
# • Saves the text to a .txt file.
# • Includes ‘Save’ and ‘Exit’ buttons.
import tkinter as tk
from tkinter import filedialog

def save_text():
    text = text_box.get("1.0", tk.END)
    if text.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files", "*.txt"),
                                                              ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text)
            print(f"Text saved to {file_path}")
    else:
        print("No text to save.")
def exit_editor():
    root.destroy()
# Create the main window
root = tk.Tk()
root.title("Simple Text Editor")
# Create a Text widget
text_box = tk.Text(root, wrap='word', font=("Arial", 12))
text_box.pack(expand=True, fill='both', padx=10, pady=10)
# Create Save and Exit buttons
save_button = tk.Button(root, text="Save", command=save_text)
save_button.pack(side=tk.LEFT, padx=10, pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_editor)
exit_button.pack(side=tk.RIGHT, padx=10, pady=10)
# Start the main event loop
root.mainloop()
