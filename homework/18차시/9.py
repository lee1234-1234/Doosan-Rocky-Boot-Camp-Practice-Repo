import numpy as np

matrix = np.random.randint(1, 13, size=(3, 4))

print(f"원본 행렬: \n{matrix}")
print(f"각 행의 최댓값: {matrix.max(axis=1)}")