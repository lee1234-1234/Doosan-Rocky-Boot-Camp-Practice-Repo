# bfs1.py

queue = list()
visited = list()
queue.append(start_node)

while queue:
    node = queue.pop(0)
    
    if node not in visited:
        queue.extend(graph[node])
        visited.append(node)