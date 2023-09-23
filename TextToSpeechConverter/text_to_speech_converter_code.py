import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
import os

# Dictionary to map language codes to full names
language_names = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh": "Chinese",
}

def convert_to_speech():
    text = text_entry.get()
    speed = speed_scale.get()  # Get speech speed from the scale
    lang = language_var.get()  # Get selected language from the option menu
    pronunciation = pronunciation_var.get()  # Get pronunciation option

    tts = gTTS(text, lang=lang, slow=speed == 0, tld='com', lang_check=True)
    
    # Always create a new output file, ask for overwrite if it exists
    output_file = "output.mp3"
    if os.path.exists(output_file):
        result = messagebox.askyesno("Overwrite?", "The output file already exists. Do you want to overwrite it?")
        if not result:
            return

    tts.save(output_file)
    if pronunciation:
        os.system(f"start {output_file}")

def play_speech():
    playsound("output.mp3")

def clear_text():
    text_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Text to Speech Converter")

# Increase window size by double
window_width = 600
window_height = 400

# Calculate screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x, y coordinates to center the main window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a label
label = tk.Label(root, text="Enter Text:")
label.pack()

# Create a text input field
text_entry = tk.Entry(root, width=50)
text_entry.pack()

# Create a speech speed scale
speed_label = tk.Label(root, text="Speech Speed")
speed_label.pack()
speed_scale = tk.Scale(root, from_=0, to=1, orient=tk.HORIZONTAL, label="Slow  Fast")
speed_scale.pack()

# Create an option menu for language selection with full names
language_label = tk.Label(root, text="Select Language")
language_label.pack()
language_var = tk.StringVar()
language_var.set("en")  # Default language is English
language_menu = tk.OptionMenu(root, language_var, *[(code, name) for code, name in language_names.items()])
language_menu.pack()

# Create a Pronunciation checkbox
pronunciation_var = tk.BooleanVar()
pronunciation_checkbox = tk.Checkbutton(root, text="Pronunciation", variable=pronunciation_var)
pronunciation_checkbox.pack()

# Create a Convert button
convert_button = tk.Button(root, text="Convert", command=convert_to_speech)
convert_button.pack()

# Create a Play button
play_button = tk.Button(root, text="Play", command=play_speech)
play_button.pack()

# Create a Clear button
clear_button = tk.Button(root, text="Clear Text", command=clear_text)
clear_button.pack()

# Run the Tkinter main loop
root.mainloop()
