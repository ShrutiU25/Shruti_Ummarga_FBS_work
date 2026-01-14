#1. Develop a simple login system with a username and password field.
#Implement user authentication, and show a success message if the login is successful, or an error message if the login fails.

import tkinter as tk
from tkinter import messagebox

# Predefined credentials
USERNAME = "admin"
PASSWORD = "12345"

def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Login Success", "Login Successful!")
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

# Create main window
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

# Username Label & Entry
tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

# Password Label & Entry
tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

# Login Button
tk.Button(root, text="Login", command=login).pack(pady=15)

# Run application
root.mainloop()
