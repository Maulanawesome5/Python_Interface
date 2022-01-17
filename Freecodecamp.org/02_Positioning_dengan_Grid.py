# import modul tkinter untuk membangun aplikasi GUI
from tkinter import * # impor semuanya

root = Tk() # Top level widget

# Widget label untuk menampilkan tulisan
myLabel1 = Label(master=root, text="Hello World!")
myLabel2 = Label(master=root, text="My Name is Aji")
myLabel3 = Label(master=root, text="<-- this is column -->")

# Menggunakan method grid() untuk positioning
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

# method mainloop() untuk menampilkan aplikasi
root.mainloop()