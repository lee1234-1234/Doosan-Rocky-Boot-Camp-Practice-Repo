row_size = int(input("세로 크기 입력: "))
col_size = int(input("가로 크기 입력: "))

maze = []

for i in range(row_size):
    row = list(map(int, input(f"{i + 1}번째 행 입력: ").split()))
    maze.append(row)

for row in maze:
    print(row)