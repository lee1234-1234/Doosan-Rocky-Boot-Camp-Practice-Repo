# 7. tips 데이터셋의 요일별 전체금액 박스플롯 그리기

import seaborn as sns
import matplotlib.pyplot as plt

# tips 데이터셋 불러오기
tips = sns.load_dataset("tips")

# 요일(day) 별 전체금액(total_bill) 박스플롯
sns.boxplot(data=tips, x="day", y="total_bill")

# 그래프 출력
plt.show()