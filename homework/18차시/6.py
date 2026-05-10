# 6. data.csv라는 파일이 주어졌을 때, 
# 해당 데이터를 불러와서 기초 통계를 계산하는 프로그램을 작성하세요. 
# pandas를 사용하여 data.csv를 불러오고, 
# 각 열의 평균(mean), 최댓값(max), 최솟값(min) 을 출력하세요.

# 입력 예시 (data.csv)
# Name Age Salary
# Alice 25 50000
# Bob 30 60000
# Carol 28 55000
# Dave 35 70000

# 출력 결과: 
# Age 평균: 29.5, 최댓값: 35, 최솟값: 25
# Salary 평균: 58750.0, 최댓값: 70000, 최솟값: 50000

import pandas as pd

# data.csv 파일 불러오기
df = pd.read_csv("data.csv")

# Age 열 통계 출력
print(f"Age 평균: {df['Age'].mean()}, 최댓값: {df['Age'].max()}, 최솟값: {df['Age'].min()}")

# Salary 열 통계 출력
print(f"Salary 평균: {df['Salary'].mean()}, 최댓값: {df['Salary'].max()}, 최솟값: {df['Salary'].min()}")