# np_module.py

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

print(arr.shape)    # 배열의 모양
print(arr.dtype)    # 데이터 타입

print("0으로 초기화된 배열--------------")
# ones/zeros는 수치 계산 최적화를 위해 float64가 기본
zeros = np.zeros((3,3))      # 3행3열
# zeros = np.zeros((3,3), dtype=int)
print(zeros)
print(type(zeros))          # numpy.ndarray

print("1로 초기화된 배열--------------")
ones = np.ones((2,4))       # 2행4열
print(ones)
print(ones.shape)           # (2, 4)
print(ones.dtype)           # float64

print("값으로 채운 배열--------------")
full = np.full((2,2), 7, dtype=float)
print(full)

print("단위행렬--------------")
identity1 = np.eye(2, 3)    # 직사각형에서도 대각선 1을 채울 수 있음
print(identity1)

identity2 = np.identity(3)  # 3행 3열
print(identity2)

print("난수배열--------------")
# 0이상 1미만 범위의 실수 난수 생성
random = np.random.rand(3, 3)
print(random)
print(random.shape)
print(random.dtype)

# 0이상 10미만 범위의 정수 난수 생성
randint = np.random.randint(1, 10, (3, 3))
print(randint)

print("기본 산술 연산--------------")
arr = np.array([1, 2, 3, 4])
print(arr + 5)
print(arr * 2)

print("통계 함수--------------")
print(arr.sum())    # 총합
print(arr.mean())   # 평균
print(arr.max())    # 최대값
print(arr.min())    # 최소값

print("브로드캐스팅--------------")
arr1 = np.array([1, 2, 3])      # 행 백터 (3, ) => (1,3)확장
print(arr1)
print(arr1.shape)
arr2 = np.array([[1],           # 열 백터 (3,1)
                [2],
                [3]])
print(arr2)
print(arr2.shape)

# 브로드캐스팅(virtual expansion)
# : 자동으로 (모양을) 맞춰서 늘려준다.
# arr1은 1차원이지만 연산시 (1,3) 처럼 동작

result = arr1 + arr2
print(result)
print(result.shape)

# [[1 2 3]     [[1 1 1]     [[2 3 4]
#  [1 2 3]  +   [2 2 2]  =   [3 4 5]
#  [1 2 3]]     [3 3 3]]     [4 5 6]]

print("--------------")
# 행렬 곱
matrix1 = np.array([[1,2], [3,4]])
matrix2 = np.array([[5,6], [7,8]])
result = np.dot(matrix1, matrix2)
print(result)

print("기본 인덱싱--------------")
arr = np.array([10,20,30,40])
print(arr[2])
arr = np.array([[1,2,3],
                [4,5,6]])
print(arr[1,2])

print("슬라이싱--------------")
print(arr[0,:])
print(arr[:,1])

print("조건부 연산--------------")
arr = np.array([1,2,3,4,5])
filtered = arr[arr>3]
print(filtered)


import pandas as pd
df = pd.DataFrame(arr, columns=['Value'])
print(df)
print(type(df))     # <class 'pandas.DataFrame'>