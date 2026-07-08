import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Enter a valid password length!")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))

        result.config(state="normal")
        result.delete(0, tk.END)
        result.insert(0, password)
        result.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Please enter a number!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#2C3E50")

title = tk.Label(root, text="🔐 Password Generator",
                 font=("Arial", 18, "bold"),
                 bg="#2C3E50", fg="white")
title.pack(pady=15)

tk.Label(root, text="Password Length:",
         font=("Arial", 12),
         bg="#2C3E50", fg="white").pack()

length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password",
          font=("Arial", 12, "bold"),
          bg="#27AE60", fg="white",
          command=generate_password).pack(pady=10)

result = tk.Entry(root, font=("Arial", 12), width=30,
                  justify="center", state="readonly")
result.pack(pady=10)

root.mainloop()
