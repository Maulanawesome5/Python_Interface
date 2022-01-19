from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Top level widget
root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')

def popup():
    # method dalam messagebox --> showinfo(), showwarning(), showerror()
    # askquestion(), askcancel(), askyesno()
    # response = messagebox.showinfo(title="This is my Popup", message="Hello World !")
    response = messagebox.askyesno(title="This is my Popup", message="Hello World !")
    
    Label(root, text=response).pack()
    
    if response == 1:
        Label(root, text="You cliked Yes !").pack()
    else:
        Label(root, text="You cliked No").pack()

Button(root, text="Popup", command=popup).pack()




root.mainloop()