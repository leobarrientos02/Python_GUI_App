import tkinter as tk
from tkinter import filedialog, Text
import os

# Root
root = tk.Tk()

# Functions


def addApp():
    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))


# Canvas
canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
# Attach to the root
canvas.pack()

# Frame
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Button
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg='white', bg="#263D42", command=addApp)
openFile.pack()

# Button RunApps
runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg='white', bg="#263D42")
runApps.pack()

# RUN THE GUI
root.mainloop()
