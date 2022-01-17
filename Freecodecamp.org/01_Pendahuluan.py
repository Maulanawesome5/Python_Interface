# import modul tkinter untuk membangun aplikasi GUI
from tkinter import * # impor semuanya

root = Tk() # Top level widget

# Widget label untuk menampilkan tulisan
myLabel = Label(master=root, text="Hello World!")

# Menggunakan method pack() untuk positioning
myLabel.pack() #Shoving it onto the screen

# method mainloop() untuk menampilkan aplikasi
root.mainloop()