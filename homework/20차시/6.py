# 6. seaborn을 사용하여 임의의 데이터를 생성하고 히스토그램 그리기

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 평균이 50, 표준편차가 10인 정규 분포 데이터 1000개 생성
data = np.random.normal(loc=50, scale=10, size=1000)

# 히스토그램 시각화
sns.histplot(data, kde=True)

# 그래프 출력
plt.show()