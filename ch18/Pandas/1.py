# 1.py
import pandas as pd

data = {
    'ID': [1 ,2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 35, 25]
}

df = pd.DataFrame(data)
print(df)

print("열 선택--------------")
print(df['Name'])
print(type(df['Name']))
print(df['Age'])

print("조건 필터링--------------")
print(df['Age'] > 30)
print(type(df['Age'] > 30))

print("필터링--------------")
print(df[df['Age'] > 30])
print(type(df[df['Age'] > 30]))