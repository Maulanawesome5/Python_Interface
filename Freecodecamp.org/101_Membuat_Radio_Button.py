from tkinter import *
from PIL import ImageTk, Image

# Top level widget
root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')

# Variabel ini akan terhubung dengan parameter 'variabel' dan 'value'
# gunanya jika kita hendak memilih sesuatu, maka 'value' akan ditangkap
# sebagai pilihan yang dipilih oleh user dan bisa melakukan aksi tertentu
# r = IntVar()
# r.set("2")

TOPPING = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

# Membuat radio button menggunakan for loop, agar jumlah radio button
# otomatis mengikuti jumlah isi data
for text, topping in TOPPING:
    Radiobutton(master=root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    myLabel = Label(master=root, text=value).pack()


# Membuat button
myButton = Button(master=root, text="Click me!", command=lambda: clicked(pizza.get())).pack()


root.mainloop()