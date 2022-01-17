from tkinter import *

root = Tk() # Top level widget

# Entry adalah widget untuk memberi input
entryBox = Entry(
    master=root,
    width=50, # Mengatur lebar sebanyak 50 pixel
    borderwidth=5, # Mengatur tebal garis tepi entry
)
entryBox.pack()
entryBox.insert(0, "Masukkan nama kamu") # Menampilkan tulisan dalam Entry

# Fungsi untuk melakukan aksi terhadap tombol
def myClick():
    # Variabel untuk concatenation
    hello = "Hello " + entryBox.get()
    
    myLabel = Label(
        master=root,
        # text=entryBox.get() # Menampilkan input dari Entry
        # text="Hello " + entryBox.get() # Concate dengan suatu string
        text=hello # Concate dengan variabel
    )
    myLabel.pack()

# Membuat tombol / button
myButton = Button(
    master=root,
    text="Ketik nama kamu",
    command=myClick # Menggunakan fungsi untuk melakukan sesuatu
)
myButton.pack()


root.mainloop()