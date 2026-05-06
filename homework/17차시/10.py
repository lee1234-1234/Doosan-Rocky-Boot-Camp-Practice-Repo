maze = [
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
]

def solve_maze_bfs(maze, start):
    queue = list()
    visited = list()
    queue.append(start)

    row_size = len(maze)
    col_size = len(maze[0])

    while queue:
        r, c = queue.pop(0)

        if (r, c) not in visited:
            visited.append((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < row_size and 0 <= nc < col_size:
                    if maze[nr][nc] == 0 and (nr, nc) not in visited:
                        queue.append((nr, nc))

    return visited

print(f"{solve_maze_bfs(maze, (0, 0))}")