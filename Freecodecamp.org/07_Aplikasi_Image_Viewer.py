from tkinter import *
from PIL import ImageTk, Image # Modul untuk memasukkan gambar

root = Tk() # Top level widget
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')

# Memasukkan foto ke dalam aplikasi
resolusi_foto = (500, 500) # Tipe data tuple, untuk mengubah ukuran foto jika kebesaran

my_img1 = ImageTk.PhotoImage(
    Image.open(
        'D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/kucing.jpg'
    ).resize(resolusi_foto) # Karena ukuran asli foto besar, maka digunakan method resize()
)
my_img2 = ImageTk.PhotoImage(Image.open('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/masyaallah.jpg').resize(resolusi_foto))
my_img3 = ImageTk.PhotoImage(Image.open('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/tampan1.jpg').resize(resolusi_foto))
my_img4 = ImageTk.PhotoImage(Image.open('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/tampan2.jpg').resize(resolusi_foto))
my_img5 = ImageTk.PhotoImage(Image.open('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/tampan3.jpg').resize(resolusi_foto))

# Menampung semua variabel foto ke dalam tipe data list
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Label untuk menampung gambar
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


# Untuk mengganti slide foto maju
def forward(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    
    button_next = Button(
        master=root,
        text=">>",
        command=lambda: forward(image_number+1)
    ).grid(row=1, column=2)
    
    button_back = Button(
        master=root,
        text="<<",
        command=lambda: backward(image_number-1)
    ).grid(row=1, column=0)

    if image_number == 4:
        button_next = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)


# Untuk mengganti slide foto mundur
def backward(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    
    button_next = Button(
        master=root,
        text=">>",
        command=lambda: forward(image_number+1)
    ).grid(row=1, column=2)
    
    button_back = Button(
        master=root,
        text="<<",
        command=lambda: backward(image_number-1)
    ).grid(row=1, column=0)

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)


# Tombol untuk menampilkan foto, dan exit
# mengaplikasikan grid() sistem secara shorthand
button_back = Button(master=root, text="<<", command=backward).grid(row=1, column=0)
button_exit = Button(master=root, text="EXIT PROGRAM", command=root.quit).grid(row=1, column=1)
button_next = Button(master=root, text=">>", command=lambda: forward(2)).grid(row=1, column=2)


root.mainloop()