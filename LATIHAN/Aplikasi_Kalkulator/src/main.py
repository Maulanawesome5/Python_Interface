# Membuat program untuk input angka
first_input = float(input("Masukkan angka: "))
operator = input("Pilih operator (+, -, /, *): ")
second_input = float(input("Masukkan angka: "))

# Logika kalkulator
if operator == '+':
    hasil = first_input + second_input
    print(f'{first_input} {operator} {second_input} = {hasil}')
elif operator == '-':
    hasil = first_input - second_input
    print(f'{first_input} {operator} {second_input} = {hasil}')
elif operator == '*':
    hasil = first_input * second_input
    print(f'{first_input} {operator} {second_input} = {hasil}')
elif operator == '/':
    hasil = first_input / second_input
    print(f'{first_input} {operator} {second_input} = {hasil}')


# Membuat tampilan GUI
import tkinter

root = tkinter.Tk() # top level widget
root.title = 'Kalkulator versi Aji'

# Membuat teks entry
first_input = tkinter.Entry(master=root)
first_input.grid(row=0, column=0, sticky=tkinter.W) # Menaruh di kolom 1 baris 1

input_operator = tkinter.Entry(master=root)
input_operator.grid(row=0, column=1, sticky=tkinter.W) # Menaruh di kolom 1 baris 2

second_input = tkinter.Entry(master=root)
second_input.grid(row=0, column=2, sticky=tkinter.W) # Menaruh di kolom 1 baris 3



# Render aplikasi
root.mainloop()