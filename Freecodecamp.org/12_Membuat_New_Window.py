from tkinter import *
from PIL import ImageTk, Image

# Top level widget
root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')

def opens():
    global my_img # Membuat variabel global agar foto bisa muncul di second window

    # Membuat top level window
    top = Toplevel()
    top.title('My second window')
    top.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
    
    # Menambahkan gambar, dan mengatur resolusi foto
    resolusi = (500, 500)
    my_img = ImageTk.PhotoImage(
        Image.open(
            'D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/tampan1.jpg',
        ).resize(resolusi)
    )

    # Foto akan ditampilkan dalam label widget
    myLabel = Label(master=top, image=my_img).pack()

    # Membuat tombol keluar dari second window
    tombol_exit = Button(master=top, text="Close window", command=top.destroy).pack()


tombol = Button(master=root, text="Buka gambar", command=opens).pack()



root.mainloop()