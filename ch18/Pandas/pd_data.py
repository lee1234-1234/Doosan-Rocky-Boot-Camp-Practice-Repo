# pd_data.py
import pandas as pd

path = r'ch18\Pandas\data.csv'
df_csv = pd.read_csv(path, header=None)
print(type(df_csv))
print(df_csv)

print("-----------------")
path1 = r'ch18\Pandas\data.xlsx'
df_xl = pd.read_excel(path1)
print(type(df_xl))
print(df_xl)


print("HEAD-----------------")
print(df_csv.head())
print(df_csv.head(3))

print("TAIL-----------------")
print(df_csv.tail())
print(df_csv.tail(2))

print("INFO-----------------")
df_csv.info()       # 데이터 요약 정보

# 객체 타입
# 행 정보
# 열 정보
# (컬럼번호, 컬럼명, 비어있지 않은 데이터 개수, 데이터 타입)
# 메모리

print("DESCRIBE-----------------")
# 기술 통계량 정보
print(df_csv.describe())

print("SAMPLE-----------------")
# 랜덤 샘플링(개수 or 비율)

print(df_csv.sample(2))
print("-----------------")
print(df_csv.sample(frac=0.5))