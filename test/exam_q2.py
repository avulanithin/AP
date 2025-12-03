from tkinter import *

def add():
    result.set(float(num1.get()) + float(num2.get()))

def sub():
    result.set(float(num1.get()) - float(num2.get()))

def mul():
    result.set(float(num1.get()) * float(num2.get()))

def div():
    if float(num2.get()) != 0:
        result.set(float(num1.get()) / float(num2.get()))
    else:
        result.set("Error")

root = Tk()
root.title("Simple Calculator")

num1 = Entry(root)
num1.pack()

num2 = Entry(root)
num2.pack()

Button(root, text="+", command=add).pack()
Button(root, text="-", command=sub).pack()
Button(root, text="*", command=mul).pack()
Button(root, text="/", command=div).pack()

result = StringVar()
Label(root, textvariable=result).pack()

root.mainloop()
