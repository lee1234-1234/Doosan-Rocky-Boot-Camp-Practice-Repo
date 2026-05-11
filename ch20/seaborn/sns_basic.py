# sns_basic.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로그
iris = sns.load_dataset("iris")
# print(type(iris))
# print(iris)

# 2. 기본 스타일 설정
sns.set_theme(style="whitegrid")    # 배경

# 3. 그래프 표시
sns.scatterplot(data=iris, 
                x='sepal_length',
                y='sepal_width',
                hue='species')
plt.show()