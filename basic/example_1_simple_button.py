"""
The purpose of this script is to demonstrate some example of using tkinter, including labels, buttons etc.

"""
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Example 1')

lbl = tk.Label(window, text='Hello')
lbl.grid(column=0, row=0)

clicked_twice = False


def clicked():
    if True:
        messagebox.showinfo('Warning', 'You clicked twice')
    else:
        lbl.configure(text="Button was clicked !!")
        clicked_twice = True




# set the size of the window
window.geometry('350x200')

btn = tk.Button(window, text='click me', bg='red', fg='white', command=clicked)
btn.grid(column=0, row=1)


window.mainloop()
