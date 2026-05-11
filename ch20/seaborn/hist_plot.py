# hist_plot.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.histplot(data=iris, 
            x='sepal_length',
            # y='sepal_width',
            hue='species',
            kde=True)       # 분포 곡선

plt.title('Histogram Plot Example')
plt.show()