# plt_module.py

import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams["font.family"] = "Malgun Gothic"

# print("---------------------")
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# plt.hist(data, bins=4, color="skyblue", edgecolor="black")
# plt.title("히스토그램")
# plt.show()

# print("---------------------")
# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
# y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
# plt.scatter(x, y, color="green")
# plt.title("Scatter Plot")
# plt.show()

# print("---------------------")
# sizes = [15, 30, 45, 10]
# labels = ["Group A", "Group B", "Group C", "Group D"]
# plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
# plt.title("Pie Chart")
# plt.show()

# print("---------------------")
# data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8, 50]
# plt.boxplot(data)
# plt.title("Box Plot")
# plt.show()

# print("---------------------")
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 35]
# plt.plot(x, y, color="red", linestyle="--", marker="o")
# plt.title("Customized Line Plot")
# plt.show()

# linestyle : '-' ':' '-.' '--'
# marker : '.' ',' 'o' '^' 'v'

print("---------------------")
x = [1, 2, 3, 4]
y = [10, 20, 25, 35]
plt.plot(x, y, "k^:")
plt.xlim(0, 5)
plt.ylim(0, 40)
plt.xticks(range(1, 5))
plt.yticks(range(0, 41, 10))
plt.show()

# xlim : x축 표시 범위
# ylim : y축 표시 범위
# xticks : x축 눈금
# yticks : y축 눈금