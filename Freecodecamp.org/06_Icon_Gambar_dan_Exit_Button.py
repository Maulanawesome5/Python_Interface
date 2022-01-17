from tkinter import *
from PIL import ImageTk, Image # Modul untuk memasukkan gambar

root = Tk() # Top level widget
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
# Method iconbitmap() hanya mendukung gambar/icon dengan format .ico
# kalau bisa harus desain dulu, atau download dari internet

# Memasukkan foto ke dalam aplikasi
resolusi_foto = (500, 500) # Tipe data tuple, untuk mengubah ukuran foto jika kebesaran

my_img = ImageTk.PhotoImage(
    Image.open(
        'D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/tampan1.jpg'
    ).resize(resolusi_foto) # Karena ukuran asli foto besar, maka digunakan method resize()
)

my_label = Label(image=my_img)
my_label.pack()
# my_label.grid(row=0, column=0)

# Membuat tombol untuk exit aplikasi
button_quit = Button(master=root, text="Pencet untuk keluar", command=root.quit)
button_quit.pack()
# button_quit.grid(row=0, column=1)

root.mainloop()