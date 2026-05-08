# plt_module.py

import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams["font.family"] = "Malgun Gothic"

print("---------------------")
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color="skyblue", edgecolor="black")
plt.title("히스토그램")
plt.show()

