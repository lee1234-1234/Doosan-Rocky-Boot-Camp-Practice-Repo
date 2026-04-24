from tkinter import Tk
from tkinter import Button
from tkinter import Radiobutton
from tkinter import IntVar

otk = Tk()
otk.geometry("300x200")

def order():
    print("주문합니다.")

oradio1 = Radiobutton(otk, text="A 런치")
oradio2 = Radiobutton(otk, text="B 런치")
oradio3 = Radiobutton(otk, text="C 런치")
oradio1.pack()
oradio2.pack()
oradio3.pack()

obtn1 = Button(otk, text="주문", command=order)
obtn1.pack()

otk.mainloop()