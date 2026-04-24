from tkinter import Tk
from tkinter import Button
from tkinter import BooleanVar
from tkinter import Checkbutton

otk = Tk()
otk.geometry("300x200")

coffee = {0:"아메리카노", 1:"라떼", 2:"카푸치노런치", 3:"에스프레소"}

check_value = {}    # 빈 딕셔너리

# 불리언 변수 4개 생성
for i in range(len(coffee)):
    check_value[i] = BooleanVar()
    
print("chekc_value", check_value)

for i in range(len(coffee)):
    ocheckbutton = Checkbutton(otk, text=coffee[i], variable=check_value[i])
    ocheckbutton.pack() # 위젯 배치

def buy():
    print("다음 메뉴를 주문합니다.")
    for i in range(len(coffee)):
        if check_value[i].get():
            print(coffee[i])

obtn1 = Button(otk, text="주문", command=buy)

obtn1.pack()

otk.mainloop()