#2. Build a currency converter application that converts between different currencies.
#The user should be able to enter an amount, select the input currency, select the output currency, and see the converted amount.

import tkinter as tk
from tkinter import messagebox

# Conversion rates (base: INR)
rates = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}

def convert():
    try:
        amount = float(entry_amount.get())
        from_cur = from_currency.get()
        to_cur = to_currency.get()

        # Convert amount
        result = (amount * rates[from_cur]) / rates[to_cur]
        lbl_result.config(text=f"Converted Amount: {result:.2f} {to_cur}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount")


# Main Window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x300")

# Amount
tk.Label(root, text="Enter Amount").pack(pady=5)
entry_amount = tk.Entry(root)
entry_amount.pack()

# From Currency
tk.Label(root, text="From Currency").pack(pady=5)
from_currency = tk.StringVar(value="INR")
tk.OptionMenu(root, from_currency, *rates.keys()).pack()

# To Currency
tk.Label(root, text="To Currency").pack(pady=5)
to_currency = tk.StringVar(value="USD")
tk.OptionMenu(root, to_currency, *rates.keys()).pack()

# Convert Button
tk.Button(root, text="Convert", command=convert).pack(pady=15)

# Result Label
lbl_result = tk.Label(root, text="Converted Amount: ")
lbl_result.pack(pady=10)

# Run App
root.mainloop()
