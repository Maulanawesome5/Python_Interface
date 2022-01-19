from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# Top level widget
root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')

# variabel raw string untuk menyimpan alamat file
lokasi_file = r'D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon'

def open():
    global my_img
    # mengakses lokasi folder
    root.filename = filedialog.askopenfilename(
        initialdir=lokasi_file,
        title="Select A File",
        filetypes=(("jpg files", "*.jpg"), ("all files", "*.*"))
    )

    # Mengakses file foto
    resolusi = (500, 500)
    my_img = ImageTk.PhotoImage(Image.open(root.filename).resize(resolusi))
    my_img_label = Label(image=my_img).pack()
    my_label = Label(master=root, text=root.filename).pack()


my_button = Button(master=root, text="Open File", command=open).pack()

root.mainloop()
