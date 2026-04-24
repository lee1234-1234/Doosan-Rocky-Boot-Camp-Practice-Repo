from tkinter import Tk
from tkinter import Button
from tkinter import BooleanVar
from tkinter import Checkbutton

otk = Tk()
otk.geometry("300x200")

coffee = {0:"아메리카노", 1:"라떼", 2:"카푸치노런치", 3:"에스프레소"}

check_value1 = BooleanVar()
check_value2 = BooleanVar()
check_value3 = BooleanVar()
check_value4 = BooleanVar()

# check_value1.set(True)
# check_value2.set(True)
# check_value3.set(True)
# check_value4.set(True)

ocheckbutton1 = Checkbutton(otk, text=coffee[0], variable=check_value1)
ocheckbutton2 = Checkbutton(otk, text=coffee[1], variable=check_value2)
ocheckbutton3 = Checkbutton(otk, text=coffee[2], variable=check_value3)
ocheckbutton4 = Checkbutton(otk, text=coffee[3], variable=check_value4)

def buy():
    print("다음 메뉴를 주문합니다.")
    val1 = check_value1.get()  # 정수값 접근
    val2 = check_value2.get()  # 정수값 접근
    val3 = check_value3.get()  # 정수값 접근
    val4 = check_value4.get()  # 정수값 접근
    if val1:
        print(coffee[0])
    if val2:
        print(coffee[1])
    if val3:
        print(coffee[2])
    if val4:
        print(coffee[3])

obtn1 = Button(otk, text="주문", command=buy)

ocheckbutton1.pack()
ocheckbutton2.pack()
ocheckbutton3.pack()
ocheckbutton4.pack()
obtn1.pack()

otk.mainloop()