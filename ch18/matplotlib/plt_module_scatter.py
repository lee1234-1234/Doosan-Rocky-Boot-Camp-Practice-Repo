# plt_module.py

import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams["font.family"] = "Malgun Gothic"

print("---------------------")
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# plt.hist(data, bins=4, color="skyblue", edgecolor="black")
# plt.title("히스토그램")
# plt.show()

print("---------------------")
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
plt.scatter(x, y, color="green")
plt.title("Scatter Plot")
plt.show()
