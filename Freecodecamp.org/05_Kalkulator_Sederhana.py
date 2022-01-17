from tkinter import *

root = Tk() # Top level widget
root.title("Kalkulator Sederhana") # Memberi judul aplikasi

# Entry untuk memasukkan angka
entryBox = Entry(
    master=root,
    width=35,
    borderwidth=5
)
entryBox.grid(
    row=0,
    column=0,
    columnspan=3,
    padx=10,
    pady=10
)

# Fungsi untuk memasukkan angka ke Entry
def button_click(number):
    current = entryBox.get()
    entryBox.delete(0, END)
    entryBox.insert(0, str(current) + str(number))


# Fungsi untuk menghapus input pada Entry
def button_clear():
    entryBox.delete(0, END)


# Fungsi untuk menjumlahkan angka
def button_add():
    first_number = entryBox.get() # Variabel untuk menyimpan angka yang pertama dimasukkan
    global f_num # Global scope variabel, untuk bisa di masukkan ke fungsi aritmatika lainnya
    global math # Global scope variabel, untuk bisa di masukkan ke fungsi aritmatika lainnya
    math = "addition"
    f_num = int(first_number) # Casting tipe data, untuk angka yang pertama dimasukkan
    entryBox.delete(0, END)


# Fungsi sama dengan untuk menampilkan hasil penjumlahan
def button_equal():
    second_number = entryBox.get() # Variabel untuk menyimpan angka yang kedua dimasukkan
    entryBox.delete(0, END)
    if math == "addition":
        entryBox.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        entryBox.insert(0, f_num - int(second_number))
    
    if math == "multiplication":
        entryBox.insert(0, f_num * int(second_number))
    
    if math == "division":
        entryBox.insert(0, f_num / int(second_number))


# Fungsi untuk operasi pengurangan
def button_subtract():
    first_number = entryBox.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entryBox.delete(0, END)


# Fungsi untuk operasi perkalian
def button_multiply():
    first_number = entryBox.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entryBox.delete(0, END)


# Fungsi untuk operasi pembagian angka
def button_divide():
    first_number = entryBox.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entryBox.delete(0, END)

# Membuat widget tombol angka
button1 = Button(
    master=root,
    text="1",
    padx=40,
    pady=20,
    # Lambda digunakan untuk mengirim input berupa angka ke method button_click()
    command=lambda: button_click(1)
)
button2 = Button(master=root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(master=root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(master=root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(master=root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(master=root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(master=root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(master=root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(master=root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(master=root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Tombol operator aritmatika dan hapus layar
button_add = Button(master=root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(master=root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(master=root, text="Clear", padx=79, pady=20, command=button_clear)

button_subtract = Button(master=root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(master=root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(master=root, text="/", padx=41, pady=20, command=button_divide)


# Menaruh button ke layar
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

# Tombol operator aritmatika dan hapus layar
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)



root.mainloop()