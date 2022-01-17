from tkinter import *

root = Tk() # Top level widget

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

# Membuat tombol / button
myButton = Button(
    master=root,
    text="Click Me!",
    # state=DISABLED, # agar tombol tidak bisa di klik
    padx=50, # padx / padding x mengatur lebar ke samping
    pady=10, # pady / padding y mengatur lebar ke atas
    command=myClick, # Menggunakan fungsi untuk melakukan sesuatu
    fg="blue", # Mewarnai tulisan pada tombol
    bg="yellow" # Mewarnai tombol
)
myButton.pack()

root.mainloop()