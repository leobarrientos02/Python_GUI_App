import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter.font import BOLD

# Root
root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        # print(tempApps)
        apps = [x for x in tempApps if x.strip()]

# Functions


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    # print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


# Canvas
canvas = tk.Canvas(root, height=500, width=600, bg="#263D42")
# Attach to the root
canvas.pack()

# Frame
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

# Button
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg='white', bg="#263D42", command=addApp)
openFile.pack()

# Button RunApps
runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg='white', bg="#263D42", command=runApps)
runApps.pack()

# Design
txt1 = tk.Label(frame, text="My Apps", font=('Arial', 12, 'bold', 'underline'))
txt1.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

# RUN THE GUI
root.mainloop()

# Save the file
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
