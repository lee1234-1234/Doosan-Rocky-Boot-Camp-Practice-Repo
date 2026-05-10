from scipy.stats import describe

group_A = [80, 85, 90, 75, 95]

stats = describe(group_A)

print(f"데이터 개수: {stats.nobs}")
print(f"최솟값: {stats.minmax[0]}")
print(f"최댓값: {stats.minmax[1]}")
print(f"평균: {stats.mean}")
print(f"분산: {stats.variance}")
print(f"왜도: {stats.skewness}")
print(f"첨도: {stats.kurtosis}")