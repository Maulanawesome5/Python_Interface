from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
root.geometry('400x400')


# create submit function for database
def submit():
    # Database
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Membuat cursor
    c = conn.cursor()

    # Membuat table
    # c.execute("""CREATE TABLE address (
    #     first_name text,
    #     last_name text,
    #     address text,
    #     city text,
    #     state text,
    #     zipcode integer
    # )""")

    # Insert into table
    c.execute(
        "INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        }
    )

    # Clear the textbox
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    conn.commit() # commit change to database
    conn.close() # close connection from database



# Query method
def query():
    # Database
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Membuat cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM address")
    records = c.fetchall()
    print(records)

    # Loop thru results
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit() # commit change to database
    conn.close() # close connection from database


# Membuat textbox
f_name = Entry(root, width=30).grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30).grid(row=1, column=1)
addr = Entry(root, width=30).grid(row=2, column=1)
city = Entry(root, width=30).grid(row=3, column=1)
states = Entry(root, width=30).grid(row=4, column=1)
zipcode = Entry(root, width=30).grid(row=5, column=1)

# Membuat textbox label
f_name_label = Label(master=root, text="First Name").grid(row=0, column=0)
l_name_label = Label(master=root, text="Last Name").grid(row=1, column=0)
addr_label = Label(master=root, text="Address").grid(row=2, column=0)
city_label = Label(master=root, text="City").grid(row=3, column=0)
states_label = Label(master=root, text="States").grid(row=4, column=0)
zipcode_label = Label(master=root, text="Zipcode").grid(row=5, column=0)

# Create submit button
submit_btn = Button(
    master=root,
    text="Add record to database",
    command=submit
).grid(row=6, column=0, columnspan=2, pady=10, ipadx=100)

# Create query button
query_btn = Button(
    master=root,
    text="Show records",
    command=query
).grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)





root.mainloop()