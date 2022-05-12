# from tkinter import*
# from PIL import ImageTk,Image

# root = Tk()
# root.title("Hello ! ")
# root.iconbitmap('C:\on.png')

# root.mainloop()

from tkinter import *
from PIL import Image,ImageTk
gui= Tk()

width =100
height =100
photo= Image.open("on.png")
photo= photo.resize((width, height),Image.ANTIALIAS)
# create an object of PhotoImage
photoImg = ImageTk.PhotoImage(photo)
photo_label= Label(gui, image=photoImg)
photo_label.pack()
gui.mainloop()