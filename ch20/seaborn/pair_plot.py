# pair_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.pairplot(iris, hue='species')       # 분포 곡선

plt.title('Pairplot Plot Example')
plt.show()