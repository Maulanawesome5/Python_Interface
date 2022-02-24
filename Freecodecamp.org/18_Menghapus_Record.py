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

# Function untuk menghapus record
def delete():
    # Membuat database baru atau menyambung ke database yang ada
    conn = sqlite3.connect('address_book.db')

    # Membuat cursor
    c = conn.cursor()

    # Menghapus record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    conn.commit() # commit setiap perubahan
    conn.close() # close connection dari database setelah selesai


# create submit function for database
def submit():
    # Membuat database baru atau menyambung ke database yang ada
    conn = sqlite3.connect('address_book.db')

    # Membuat cursor
    c = conn.cursor()

    # # Membuat table
    # # Tipe data yang terdapat pada SQLite3 = text, integer, real (desimal), null, blob (image, audio, video)
    # c.execute("""CREATE TABLE addresses (
    #     first_name text,
    #     last_name text,
    #     address text,
    #     city text,
    #     state text,
    #     zipcode integer
    #     )
    # """)

    # Insert into table
    c.execute("""INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)""",
        {   #key    : value
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        }
    )

    # Clear the textbox, setiap selesai menambah data
    # tulisan di textbox akan otomatis terhapus
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    conn.commit() # commit setiap perubahan
    conn.close() # close connection dari database setelah selesai



# Query method
def query():
    # Database
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Membuat cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses") # SELECT * artinya seleksi semua yang ada dalam tabel addresses
    records = c.fetchall()
    print(records)

    # Loop thru results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit() # commit change to database
    conn.close() # close connection from database


# Membuat textbox
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=20)
delete_box.grid(row=9, column=1, pady=5)

# Membuat textbox label
f_name_label = Label(master=root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(master=root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(master=root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(master=root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(master=root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(master=root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=9, column=0, pady=5)

# Membuat submit button untuk menambahkan data dari GUI ke database
submit_btn = Button(
    master=root,
    text="Add record to database",
    command=submit
)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)


# Membuat query button, untuk menampilkan isi database ke terminal
query_btn = Button(
    master=root,
    text="Show records",
    command=query
)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Membuat tombol untuk menghapus query
delete_btn = Button(
    master=root,
    text="Delete record",
    command=delete
)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)


conn.commit() # commit setiap perubahan
conn.close() # close connection dari database setelah selesai

root.mainloop()