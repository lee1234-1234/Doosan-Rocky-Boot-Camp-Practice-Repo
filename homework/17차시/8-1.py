maze = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
]

for row in maze:
    print(row)

# 지도의 세로, 가로 크기 입력
row_size = int(input("세로 크기 입력: "))
col_size = int(input("가로 크기 입력: "))

# 지도를 저장할 2차원 리스트
maze = []

# 행 개수만큼 반복해서 지도 데이터 입력
for i in range(row_size):
    row = list(map(int, input(f"{i + 1}번째 행 입력: ").split()))
    maze.append(row)

for row in maze:
    print(row)