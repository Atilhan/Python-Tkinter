import tkinter as tk
from tkinter import *
from unicodedata import is_normalized
root = Tk()

# schijf hier tussen je code 

global is_on 
is_on = True


#labels
my_label = Label(root, 
    text="The Switch Is On",
    fg="green",
    font=("Helveticca", 15))

my_label.pack(pady=20)

def switch():
    global is_on
    if is_on:
        on_button.config(image=off)
        my_label.config(text="The Switch Is Off ! ",fg="red")
        is_on = False
        print('Its off now ! ')
    else:
        on_button.config(image=on)
        my_label.config(text="The Switch Is On ! ",fg="green")
        is_on = True
        print('Its on now! ')

on = PhotoImage(file="on_1.png")
off = PhotoImage(file="off_2.png")

on_button = Button(root, image=on, bd=0, command=switch)
on_button.pack(pady=50)

# schijf hier tussen je code

root.mainloop()