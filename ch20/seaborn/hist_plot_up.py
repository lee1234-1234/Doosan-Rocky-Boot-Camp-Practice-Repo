# hist_plot_up.py

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

sns.set_theme(style='darkgrid',
                palette='muted')

sns.histplot(data=iris, 
            x='sepal_length',
            # y='sepal_width',
            hue='species',
            kde=True)       # 분포 곡선

plt.title('Histogram Plot Example')
plt.show()