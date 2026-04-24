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

# 2. 위젯 배치
obtn1.pack(side="top")
obtn2.pack(side="left")
obtn3.pack(side="right")

# 3. 이벤트 및 바인딩
# 누름(버튼 이벤트) 발생시, 특정 동작이 수행(바인딩)

otk.mainloop()