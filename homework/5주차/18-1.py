import pandas as pd

path = r'대구광역시 동구_연도별 체납차량 번호판 영치실적_20251031.csv'
df = pd.read_csv(path, encoding="cp949")
print(df)