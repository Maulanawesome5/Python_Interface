from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
root.geometry('400x400')

# Membuat slider
vertical = Scale(master=root, from_=0, to=200)
vertical.pack()

def slide():
    my_label = Label(master=root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


horizontal = Scale(master=root, from_=0, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()

my_label = Label(master=root, text=horizontal.get()).pack()

my_button = Button(root, text="Click Me!", command=slide).pack()






root.mainloop()