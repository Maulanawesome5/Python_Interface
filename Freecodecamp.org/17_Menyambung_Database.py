from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
root.geometry('400x400')

# Database
# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Membuat cursor
c = conn.cursor()

# Membuat table
c.execute("""CREATE TABLE address (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )"""
)

# commit change
conn.commit()

# close connection
conn.close()

root.mainloop()