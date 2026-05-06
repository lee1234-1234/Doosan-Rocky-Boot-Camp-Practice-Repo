# dfs2.py


def my_dfs(graph, start_node):
    stack = list()      # stack = []
    visited = list()    # visited = []

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            # stack.extend(graph[node])          뒤에서부터 방문
            stack.extend(reversed(graph[node])) #앞에서부터 방문(순서대로)
            visited.append(node)
    