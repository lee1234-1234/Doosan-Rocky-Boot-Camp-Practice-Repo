from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Checkbutton
from tkinter import BooleanVar

otk = Tk()
otk.geometry("400x300")
otk.title("조각 피자 주문 프로그램")

# 피자 메뉴
pizza = {
    0: "치즈 피자 (3200원)",
    1: "콤비네이션 피자 (3500원)",
    2: "불고기 피자 (3600원)"
}

# 제목
olabel1 = Label(otk, text="피자")
olabel1.pack()

# 체크 상태 저장
check_value = {}

# 체크박스 생성
for i in range(len(pizza)):
    check_value[i] = BooleanVar()
    ocheck = Checkbutton(otk, text=pizza[i], variable=check_value[i])
    ocheck.pack(anchor="w")

# 결과 출력 라벨
result_label = Label(otk, text="")

# 주문 버튼 동작
def buy():
    total = 0
    result = "주문내역:\n"

    for i in range(len(pizza)):
        if check_value[i].get():
            result += "- " + pizza[i] + "\n"

            # 가격 추출
            price_text = pizza[i].split("(")[1]
            price_text = price_text.replace("원)", "")
            price = int(price_text)

            total += price

    result += "\n총 가격: " + str(total) + "원"

    # 윈도우에 출력
    result_label.config(text=result)

# 주문 버튼
obtn1 = Button(otk, text="주문", command=buy)

obtn1.pack()
result_label.pack()

otk.mainloop()