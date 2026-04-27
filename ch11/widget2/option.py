from tkinter import Tk
from tkinter import StringVar
from tkinter import OptionMenu

otk = Tk()
otk.geometry("400x300")

options_list = ['Option1', 'Option2', 'Option3']

selected_option = StringVar()

selected_option.set(options_list[0])
# sel_option = selected_option.get()
# print(sel_option)         # 확인용

option_menu = OptionMenu(otk, selected_option, *options_list)   #options_list == 항목들
option_menu.pack()

otk.mainloop()