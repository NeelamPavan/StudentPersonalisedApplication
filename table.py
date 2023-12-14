from tkinter import *
from PIL import ImageTk,Image
master=Tk()
Image_0=Image.open("C:\\Users\\neela\\PycharmProjects\\task1\\notes.png")
be=ImageTk.PhotoImage(Image_0)
master.geometry('800x600')
lbl=Label(master,image=be).pack()
master.mainloop()