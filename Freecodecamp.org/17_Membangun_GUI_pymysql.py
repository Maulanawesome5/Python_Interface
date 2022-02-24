from tkinter import *
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

# try:
#     # execute SQL query using execute() method.
#     cursors.execute("SELECT VERSION()")

#     # Fetch a single row using fetchone() method.
#     data = cursors.fetchone()
#     Label(master=root, text=("Database version : %s " % data)).grid(row=8, column=1)

# except:
#     conn.rollback()
#     Label(master=root, text="Can't connect to Database").grid(row=8, column=1)

# sql = """INSERT INTO addresses (first_name, last_name, address, city, state, zipcode)
# VALUES ('John', 'Elder', '10 West Elm', 'Chicago', 'IL', 60610)"""

# Membuat textbox
f_name = Entry(root, width=30)
l_name = Entry(root, width=30)
address = Entry(root, width=30)
city = Entry(root, width=30)
state = Entry(root, width=30)
zipcode = Entry(root, width=30)

f_name.grid(row=0, column=1, pady=5)
l_name.grid(row=1, column=1, pady=5)
address.grid(row=2, column=1, pady=5)
city.grid(row=3, column=1, pady=5)
state.grid(row=4, column=1, pady=5)
zipcode.grid(row=5, column=1, pady=5)

# Membuat textbox label
f_name_label = Label(master=root, text="First Name")
l_name_label = Label(master=root, text="Last Name")
address_label = Label(master=root, text="Address")
city_label = Label(master=root, text="City")
state_label = Label(master=root, text="State")
zipcode_label = Label(master=root, text="Zipcode")

f_name_label.grid(row=0, column=0, padx=20, sticky=W)
l_name_label.grid(row=1, column=0, padx=20, sticky=W)
address_label.grid(row=2, column=0, padx=20, sticky=W)
city_label.grid(row=3, column=0, padx=20, sticky=W)
state_label.grid(row=4, column=0, padx=20, sticky=W)
zipcode_label.grid(row=5, column=0, padx=20, sticky=W)

def submit():
    # Koneksi ke database MySQL
    conn = pymysql.connect(
        host="localhost",
        user="testuser",
        password="test123",
        database="address_book"
    )

    # Membuat cursor
    cursors = conn.cursor()

    # sql = """INSERT INTO addresses VALUES(:first_name, :last_name, :address, :city, :state, :zipcode)""",
    # {
    #     'first_name': f_name.get(),
    #     'last_name': l_name.get(),
    #     'address': address.get(),
    #     'city': city.get(),
    #     'state': state.get(),
    #     'zipcode': zipcode.get()
    # }

    sql = "INSERT INTO addresses(first_name, last_name, address, city, state, zipcode) \
   VALUES ('%s', '%s', '%s', '%s', '%s', '%d' )" % (f_name.get(), l_name.get(), address.get(), city.get(), state.get(), int(zipcode.get()))

    # Insert data
    cursors.execute(sql)

    # Clear the textbox, setiap selesai menambah data
    # tulisan di textbox akan otomatis terhapus
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    
    try:
        # execute SQL query using execute() method.
        cursors.execute("SELECT VERSION()")

        # Fetch a single row using fetchone() method.
        data = cursors.fetchone()
        Label(master=root, text=("Database version : %s " % data)).grid(row=8, column=1)

    except:
        conn.rollback()
        Label(master=root, text="Can't connect to Database").grid(row=8, column=1)

        # # Melakukan commit dan menutup koneksi setiap selesai melakukan perubahan
        # conn.commit(), conn.close()




# Membuat submit button untuk menambahkan data dari GUI ke database
submit_btn = Button(master=root, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=1, columnspan=2, pady=5)

# Membuat query button, untuk menampilkan isi database ke terminal
query_btn = Button(master=root, text="Show records")
query_btn.grid(row=7, column=1, columnspan=2)

# Melakukan commit dan menutup koneksi setiap selesai melakukan perubahan
conn.commit(), conn.close()

# Menampilkan GUI apps
root.mainloop()