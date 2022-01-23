from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
root.geometry('400x400')

# Fungsi untuk menampilkan nilai saat mencentang checkbox
def show():
    myLabel = Label(master=root, text=variabel.get()).pack()

# Variabel ini untuk mewakili nilai dari checkbox
variabel = IntVar()

# Membuat checkbox, berfungsi untuk memilih banyak opsi
checkbox = Checkbutton(
    master=root,
    text="Check this box, I dare you!",
    variable=variabel,
    onvalue="Menyala",
    offvalue="Tidak Menyala"
)
checkbox.pack()

# Saat ditekan.. pada posisi tercentang akan menampilkan angka 1
# Saat ditekan.. jika checkbox tidak dicentang akan menampilkan angka 0
myButton = Button(master=root, text="Show selection", command=show).pack()



root.mainloop()