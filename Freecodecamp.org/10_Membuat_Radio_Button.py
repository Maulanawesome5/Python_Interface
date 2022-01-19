from tkinter import *
from PIL import ImageTk, Image

# Top level widget
root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')

# Variabel ini akan terhubung dengan parameter 'variabel' dan 'value'
# gunanya jika kita hendak memilih sesuatu, maka 'value' akan ditangkap
# sebagai pilihan yang dipilih oleh user dan bisa melakukan aksi tertentu
r = IntVar()
r.set("2")

def clicked(value):
    myLabel = Label(master=root, text=value).pack()

# Membuat radio button widget
# 'variable' dan 'value' akan terhubung dengan baris program diatas
radio1 = Radiobutton(
    master=root,
    text="Option 1",
    variable=r,
    value=1,
    command=lambda: clicked(r.get())
).pack()

radio2 = Radiobutton(
    master=root,
    text="Option 2",
    variable=r,
    value=2,
    command=lambda: clicked(r.get())
).pack()

myLabel = Label(master=root, text=r.get()).pack()
myButton = Button(master=root, text="Click me!", command=lambda: clicked(r.get())).pack()


root.mainloop()