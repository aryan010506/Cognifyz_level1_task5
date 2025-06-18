import tkinter as tk
from tkinter import messagebox

def check_palindrome():
    text = entry.get().strip().lower()

    if not text:
        messagebox.showwarning("Input Error", "Please enter a word or phrase.")
        return

    # Remove non-alphanumeric characters (optional for phrases)
    clean_text = ''.join(char for char in text if char.isalnum())
    reversed_text = clean_text[::-1]

    if clean_text == reversed_text:
        messagebox.showinfo("Result", f"✅ '{text}' is a palindrome.")
    else:
        messagebox.showinfo("Result", f"❌ '{text}' is not a palindrome.")

# GUI Setup
app = tk.Tk()
app.title("Palindrome Checker")
app.geometry("350x200")
app.resizable(False, False)

tk.Label(app, text="Enter text:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(app, width=35, font=("Arial", 11))
entry.pack(pady=5)

tk.Button(app, text="Check", command=check_palindrome, font=("Arial", 11)).pack(pady=15)

app.mainloop()
