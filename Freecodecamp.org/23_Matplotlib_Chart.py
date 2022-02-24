from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

# Top widget
root = Tk()
root.title('Tutorial from freecodecamp.org')
root.iconbitmap('D:/LATIHAN PEMROGRAMAN/PYTHON_GUI/Freecodecamp.org/icon/bitcoin.ico')
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 250000, 5000)
    plt.hist(house_prices, 50)
    plt.show()


my_button = Button(root, text="Graph It !", command=graph)
my_button.pack()

root.mainloop()