import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Database Functions")
root.resizable(False, False)

root_width = 600
root_height = 400

# find the center point
center_x = int(root.winfo_screenwidth()/2 - root_width / 2)
center_y = int(root.winfo_screenheight()/2 - root_height / 2)
# set the position of the window to the center of the screen
root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')


def button1():
    print("Button 1")


def button2():
    print("Button 2")


# place a label on the root window
message = ttk.Label(root, text="Hello, World!").pack()
button1 = ttk.Button(root, text="Button 1", command=button1).pack()
button2 = ttk.Button(root, text="Button 2", command=button2).pack()

# keep the window displaying
root.mainloop()
