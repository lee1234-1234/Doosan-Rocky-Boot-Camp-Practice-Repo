from tkinter import Tk
from tkinter import Button
from tkinter import PhotoImage
from tkinter import Label

#png 변환 방법

from PIL import Image

Image = Image.open("경로적기")
Image.save("경로적기")
print("이미지가 PNG로 변환되었습니다.")

otk = Tk()
otk.geometry("588x385")

img1 = PhotoImage(file="경로적기")

img_label = Label(otk, image=img1)
img_label.place(x=-20, y=-20)

obtn1 = Button(otk, text="PUSH1")
obtn2 = Button(otk, text="PUSH2")
obtn3 = Button(otk, text="PUSH3")

obtn1.place(x=10, y=60)
obtn2.place(x=140, y=60)
obtn3.place(x=80, y=10)

otk.mainloop()