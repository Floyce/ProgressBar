import tkinter as tk
from tkinter import ttk
import time

def start_download():
    for i in range(101):
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.05)  # Simulates download progress

root = tk.Tk()
root.title("Blacks Progress Bar")

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

download_button = tk.Button(root, text="Start Download", command=start_download)
download_button.pack()

root.mainloop()
