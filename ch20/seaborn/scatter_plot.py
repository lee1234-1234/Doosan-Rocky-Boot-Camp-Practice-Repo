# scatter_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

# 1. 샘플 데이터 셋 로그
iris = sns.load_dataset("iris")
# print(type(iris))
# print(iris)

# 2. 기본 스타일 설정
sns.set_theme(style="ticks")    # 배경

# 3. 그래프 표시
sns.scatterplot(data=iris, 
                x='petal_length',
                y='petal_width',
                hue='species',
                style='species')
plt.title('Scatter Plot Example')
plt.show()