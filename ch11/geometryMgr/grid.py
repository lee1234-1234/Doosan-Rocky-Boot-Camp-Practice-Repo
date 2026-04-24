# import tkinter          
# from tkinter import *
from tkinter import Tk
from tkinter import Button

# 1. 위젯 생성
otk = Tk()
otk.geometry("300x200")

def hello1():
    print("안녕")
    
def hello2():
    print("잘가")

def hello3():
    print("OMG")
    
obtn1 = Button(otk, text="PUSH1")
obtn2 = Button(otk, text="PUSH2")
obtn3 = Button(otk, text="PUSH3")
obtn4 = Button(otk, text="PUSH4")

# 2. 위젯 배치
obtn1.grid(row=1, column=0)
obtn2.grid(row=1, column=1)
obtn3.grid(row=0, column=4)
obtn4.grid(row=3, column=3, padx=10, pady=20)   #버튼이 10,20만큼 더 띄어져서 풀력

# 3. 이벤트 및 바인딩
otk.mainloop()