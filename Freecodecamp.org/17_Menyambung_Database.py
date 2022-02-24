from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
root.geometry('400x400')

# Database
# Membuat database baru atau menyambung ke database yang ada
conn = sqlite3.connect('address_book.db')

# Membuat cursor
c = conn.cursor()

# Membuat table
# Tipe data yang terdapat pada SQLite3 = text, integer, real (desimal), null, blob (image, audio, video)
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )
""")

# commit change, setiap melakukan perubahan atau menambah data
conn.commit()

# close connection, setelah selesai melakukan perubahan
conn.close()

root.mainloop()