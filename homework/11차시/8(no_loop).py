from tkinter import Tk
from tkinter import Label
from tkinter import Checkbutton
from tkinter import BooleanVar

otk = Tk()
otk.geometry("400x300")
otk.title("조각 피자 주문 프로그램")

olabel1 = Label(otk, text="피자")
olabel1.pack()

pizza1 = BooleanVar()
pizza2 = BooleanVar()
pizza3 = BooleanVar()

ocheck1 = Checkbutton(otk, text="치즈 피자 (3200원)", variable=pizza1)
ocheck2 = Checkbutton(otk, text="콤비네이션 피자 (3500원)", variable=pizza2)
ocheck3 = Checkbutton(otk, text="불고기 피자 (3600원)", variable=pizza3)

ocheck1.pack()
ocheck2.pack()
ocheck3.pack()

otk.mainloop()