# pd_series.py

import pandas as pd

data = [10, 20, 30]
series = pd.Series(data)
print(series)

print("-----------------")
data = {'a': 10, 'b':20, 'c':30}
series1 = pd.Series(data)
print(series1)