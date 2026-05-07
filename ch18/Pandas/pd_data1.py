# pd_data1.py

import pandas as pd

data = {
    'ID': [1, 2, 3],
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

print("데이터 정렬---------------------")
# sorted_df = df.sort_values(by='Age')
sorted_df = df.sort_values(by='Age', ascending=True)    # True:오름차순, # False:내림차순
print(sorted_df)

print("데이터 추가 및 삭제---------------------")
# 열 추가
df['Salary'] = [5000, 6000, 7000]
print(df)

print("행 추가---------------------")
# df.loc[3] = [4, 'David', 40, 80000]
df.loc[len(df)] = [4, 'David', 40, 8000]
print(df)

print("행 삭제---------------------")
df = df.drop(1)
print(df)
# 행 번호 주의
# print(len(df))
# df.loc[len(df)] = [5, 'Eva', 50, 90000]     # len(df) 데이터 update
# print(df)

print("index 재정렬---------------------")
# index 재정렬
# df1 = df.reset_index(drop=True) # 기존 번호 지우고 새로운 번호
# print(df1)

print("새 데이터프레임 생성---------------------")
data2 = {
    'ID': [5, 6],
    'Name': ['Eve', 'Frank'],
    'Age': [28, 33]
}
df2 = pd.DataFrame(data2)
print(df2)

print("데이터 연결---------------------")
concated = pd.concat([df, df2], ignore_index=True)
print(concated)

print("데이터 병합---------------------")
# 병합 시 기준열 필요
data3 = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Department': ['HR',
                'Engineering', 
                'Sales', 
                'R&D', 
                'Finance', 
                'Sales']
}
df3 = pd.DataFrame(data3)
print(df3)

print("---------------------")
merged = pd.merge(concated, df3)
print(merged)

print("결측치 처리---------------------")
# 데이터 처리
print(merged.isnull())
print(merged.isnull().sum())

print("---------------------")
# 결측치 채우기
meanVal = merged['Salary'].mean()
print(meanVal)
merged['Salary'] = merged['Salary'].fillna(meanVal)
print(merged)

print("---------------------")
print(merged['Salary'].count())
print(merged['Salary'].std())
print(merged['Salary'].min())
print(merged['Salary'].max())
print(merged['Salary'].quantile(0.25))
print(merged['Salary'].quantile(0.50))
print(merged['Salary'].quantile(0.75))


print("---------------------")
# 특정 위치값 수정
merged.loc[4, 'Salary'] = 8500
print(merged)

print("중복 데이터 처리---------------------")
data1 = {
    'ID': [5, 6],
    'Name': ['Alice', 'Charlie'],
    'Age': [28, 33],
    'Salary': [5000, 7000],
    'Department': ['HR', 'Sales']
}
df1 = pd.DataFrame(data1)
df1 = pd.concat([merged, df1])
print(df1)
print(df1.duplicated())

print("---------------------")
df1_1 = df1.drop_duplicates()
print(df1_1)