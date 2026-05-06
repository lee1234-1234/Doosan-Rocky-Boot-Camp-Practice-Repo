# dfs1.py

stack = list()      # stack = []

visited = list()    # visited = []

start_node = ""
stack.append(start_node)

while stack:                # while에 사용가능한거 stack == [], len(stack) == 0
    node = stack.pop()
    
    if node not in visited:
        visited.append(node)
        stack.append(graph[node])
    