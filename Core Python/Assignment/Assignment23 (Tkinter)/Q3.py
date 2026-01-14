#3. Design a basic calculator to perform +,-,/,*

import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        n1 = float(entry_num1.get())
        n2 = float(entry_num2.get())

        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        elif op == '/':
            if n2 == 0:
                raise ZeroDivisionError
            result = n1 / n2

        lbl_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")


# Main Window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("350x300")

# Number 1
tk.Label(root, text="Enter First Number").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack()

# Number 2
tk.Label(root, text="Enter Second Number").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Buttons
tk.Button(root, text="+", width=5, command=lambda: calculate('+')).pack(pady=5)
tk.Button(root, text="-", width=5, command=lambda: calculate('-')).pack(pady=5)
tk.Button(root, text="*", width=5, command=lambda: calculate('*')).pack(pady=5)
tk.Button(root, text="/", width=5, command=lambda: calculate('/')).pack(pady=5)

# Result
lbl_result = tk.Label(root, text="Result: ")
lbl_result.pack(pady=15)

# Run App
root.mainloop()
