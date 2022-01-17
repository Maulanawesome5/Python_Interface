import tkinter as tk
from tkinter.constants import W

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        # self.grid()
        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.createWidgets()
    
    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        # self.quitButton.grid()
        self.quitButton.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)


app = Application()
app.master.title('Sample application')
app.mainloop()