from tkinter import *


class indo():
    def __init__(self,veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena


top = Tk()
top.geometry("200x100")
b = Button(top,text = "Ievadit informaciju")
b.pack()
Entry = Entry(Tk)
Entry.get()
top.mainloop()