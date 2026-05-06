# bfs2.py
from graph import myGraph

def my_bfs(graph, start_node):
    queue = list()                      # 1. 방문(탐색)할 노드를 담을 큐
    visited = list()                    # 2. 방문할 노드를 담을 리스트
    queue.append(start_node)            # 3. 탐색 시작 노드를 큐에 삽입

    # 6. 더 이상 방문할 노드가 없을 때까지 반복
    while queue:                        # 4. 큐에서 노드 꺼냄
        node = queue.pop(0)

        if node not in visited:         # 5. 방문하지 않았다면, 
            queue.extend(graph[node])   # 인접 노드를 큐에 삽입
            visited.append(node)        # 방문 처리
            print(f"visited: {visited}")
            print(f"queue: {queue}")
    return visited

print(my_bfs(myGraph, 'A'))

from graph1 import graph1
print(my_bfs(graph1, 3))