from distutils.util import execute
from tkinter import *
from pymysql import *
import pymysql

root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
root.geometry('400x400')

# Koneksi ke database MySQL
conn = pymysql.connect(
    host="localhost",
    user="testuser",
    password="test123",
    database="address_book"
)

# Membuat cursor
cursors = conn.cursor()

# Drop table if it already exist using execute() method.
cursors.execute("DROP TABLE IF EXISTS addresses")

try:
    # Membuat table untuk mengisi database 'address_book'
    sql = """CREATE TABLE addresses(
        first_name CHAR(20) NOT NULL,
        last_name CHAR(20) NOT NULL,
        address CHAR(20) NOT NULL,
        city CHAR(20) NOT NULL,
        state CHAR(20) NOT NULL,
        zipcode INT(6) NOT NULL
    )"""
    cursors.execute(sql) # Mengeksekusi pembuatan tabel

    cursors.execute(query="SELECT VERSION()") # Melihat versi dari database
    data = cursors.fetchone() # Fetch a single row using fetchone() method
    # print("Database version: %s " % data)
    Label(master=root, text=("Database version: %s " %data)).grid(row=1, column=0)

except:
    conn.rollback()
    Label(master=root, text="Database server not connected!").grid(row=0, column=0)


# Melakukan commit setiap selesai melakukan perubahan
conn.commit()

# Menutup koneksi setelah melakukan commit
conn.close()

# Menampilkan GUI apps
root.mainloop()