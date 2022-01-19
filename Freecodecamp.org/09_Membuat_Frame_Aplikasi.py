from tkinter import *
from PIL import ImageTk, Image

# Top level widget
root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')

# Membuat frame aplikasi
# frame menempel pada top level widget
frame = LabelFrame(master=root, text="This is my frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

# Tombol menempel pada frame widget
tombol1 = Button(master=frame, text="Don't click here!")
tombol2 = Button(master=frame, text="Please click here!")

tombol1.grid(row=0, column=0)
tombol2.grid(row=0, column=1)





root.mainloop()

# Biasanya method positioning seperti grid() dan pack() tidak bisa digabung
# dalam widget yang sama. Namun jika kita membuat frame, maka
# method positioning ini akan bisa dibuat bersamaan.
# pack() dan grid() harus dilakukan pada frame master yang berbeda