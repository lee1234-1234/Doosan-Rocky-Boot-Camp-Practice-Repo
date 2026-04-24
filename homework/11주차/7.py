from tkinter import Tk
from tkinter import Label

otk = Tk()
otk.geometry("400x300")
otk.title("조각 피자 주문 프로그램")

olable1 = Label(otk, text="피자")
olable1.pack()

otk.mainloop()