from tkinter import Tk
from tkinter import Label

otk = Tk()
otk.geometry("400x350")

olable1 = Label(otk, text="적", bg="red", width=400)
olable2 = Label(otk, text="녹", bg="green", width=400)
olable3 = Label(otk, text="파", bg="blue", width=400)

olable1.pack()
olable2.pack()
olable3.pack()

otk.mainloop()