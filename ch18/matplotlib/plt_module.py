# plt_module.py

import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams["font.family"] = "Malgun Gothic"

x = [1,2,3,4]
y= [10,20,25,30]
plt.plot(x,y)
plt.title("Line Plot")
# plt.xlabel("X-axis")
plt.xlabel("X축")
plt.ylabel("Y-axis")
plt.show()

print("---------------------")
# 막대 그래프
categories = ['A', 'B', 'C', 'D']
values = [3,7,8,5]
plt.bar(categories, values)
plt.title("막대 그래프")
plt.show()