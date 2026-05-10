import pandas as pd

df = pd.read_csv("data.csv")

print(df[(df['Age'] >= 30) & (df['Salary'] >= 60000)])