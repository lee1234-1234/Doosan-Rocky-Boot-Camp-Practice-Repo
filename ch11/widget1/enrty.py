from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import StringVar

otk = Tk()
otk.geometry("400x350")

ostring = StringVar()
oentry = Entry(otk, textvariable=ostring)   # 여기서 입력받은거를 ostring에 저장
olable = Label(otk, textvariable=ostring, bg="gold", width=20)   # ostring에 있는 내용을 label에 출력하겠다

oentry.pack()
olable.pack()

otk.mainloop()