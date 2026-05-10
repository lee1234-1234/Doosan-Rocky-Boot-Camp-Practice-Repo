import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"

path = r'대구광역시 동구_연도별 체납차량 번호판 영치실적_20251031.csv'
df = pd.read_csv(path, encoding="cp949")

df_year = df[(df['년도'] >= 2016) & (df['년도'] <= 2024)]
df_year = df_year.sort_values(by='년도')
plt.plot(df['년도'], df['영치대수'], marker = 'o')

plt.title("2016년~2024년 연도별 영치대수")
plt.xlabel("년도")
plt.ylabel("영치대수")
plt.show()