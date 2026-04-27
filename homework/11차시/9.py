from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Checkbutton
from tkinter import BooleanVar

otk = Tk()
otk.geometry("400x300")
otk.title("조각 피자 주문 프로그램")

pizza = {
    0: "치즈 피자 (3200원)",
    1: "콤비네이션 피자 (3500원)",
    2: "불고기 피자 (3600원)"
}

olabel1 = Label(otk, text="피자")
olabel1.pack()

check_value = {}

for i in range(len(pizza)):
    check_value[i] = BooleanVar()
    ocheck = Checkbutton(otk, text=pizza[i], variable=check_value[i])
    ocheck.pack(anchor="w")

obtn1 = Button(otk, text="주문")
obtn1.pack()

otk.mainloop()