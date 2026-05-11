# lmplot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.lmplot(data=iris, 
            x='sepal_length',
            y='sepal_width',
            hue='species',
            height=6)

plt.title('Lmplot Plot Example')
plt.show()

# 선 앞 반투명 음영: 회귀선의 신뢰구간((condidence Interval, CI))
# "실제 회귀선이 이 범위 안에 있을 가능성이 높다"