# p3_robot.py

# [문제] 스택을 이용한 미로 탐색
# 설명: 로봇이 미로의 입구 (0, 0)에서 출발하여 출구 (5, 5)를 향해 탐색합니다.
# 갈림길이 나오면 한 방향으로 끝까지 가보고,
# 막다른 길이면 되돌아오는 방식입니다.
# 탐색 방법: DFS   / 활용 자료 구조: stack
# [미로 지도 시각화] 0: 로봇이 갈 수 있는 길 / 1: 벽 (지나갈 수 없음)

# 미로 데이터 (2차원 리스트)
maze = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
]

def solve_maze(maze, start):
    stack = list()
    visited = list()
    stack.append(start)
    
    while stack:
        r, c = stack.pop()

        if (r, c) not in visited:
            visited.append((r,c))
            
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nc < 6 and 0 <= nr < 6 and maze[nr][nc]==0:
                    stack.append((nr,nc))
    return visited

print(f"{solve_maze(maze, (0,0))}")