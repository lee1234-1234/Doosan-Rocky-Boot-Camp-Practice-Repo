# sparse_matrix.py

from scipy.sparse import csr_matrix

data = [
    [0, 0, 3],
    [4, 0, 0],
    [0, 5, 0]
]

sparse_martix = csr_matrix(data)
print(sparse_martix)

# 평균(중심), 분산(퍼짐)
# 왜도(Skewness)는 분포의 비대칭 정도
# 첨도(Kurtosis)는 분포의 뾰족한 정도