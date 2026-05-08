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

print("---------------------")
data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8, 50]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

# 이상치(outlier): 대부분의 데이터 패턴에서 크게 벗어난 값
# 이상치 생성 이유 : 측정오류, 데이터 처리 오류, 실제 특이한 사건
# 이상치 발생시 처리 방법
# 1. 제거(삭제)
# 입력/측정/데이터 수집 오류
# 2. 값 수정(대체)
# 평균값, 중앙값, 최빈값 등으로 바꾸는 방법
# 3. 윈저라이징
# 극단값을 최대/최소 범위 값으로 바꾸는 방법
# 4. 로그 변환(데이터 변환)
# 데이터 분포를 줄이는 방법
# 5. 그대로 사용
# 이상치가 실제 의미 있는 데이터라면 그대로 사용