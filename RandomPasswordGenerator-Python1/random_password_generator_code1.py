import tkinter as tk
import random
import string
import pyperclip

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    if length < 8:
        password_label.config(text="Password length should be at least 8 characters")
        return
    
    symbols = string.punctuation
    digits = string.digits
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase

    all_characters = symbols + digits + lowercase_letters + uppercase_letters
    password = ''.join(random.choice(all_characters) for i in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    password_label.config(text="Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack()

password_entry = tk.Entry(root)
password_entry.pack(pady=10)

root.mainloop()
