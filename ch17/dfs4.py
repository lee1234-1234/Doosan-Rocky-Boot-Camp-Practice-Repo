# dfs4.py

# 매개변수: 그래프
# 반환값: 방문한리스트

myGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F']
}

start_node = 'A'
def my_dfs(graph, start_node):
    # 1. 탐색할 노드를 담을 스택
    stack = list() 
    
    # 2. 방문 여부 확인 리스트
    visited = list()

    # 3. 탐색 시작 노드
    stack.append(start_node)
    
    # 6. 4~5번 과정 반복
    while stack:
        # 4. 방문할 노드를 스택에서 제거
        node = stack.pop()

        # 5. 방문 리스트에 스택에서 꺼낸 노드가 없으면
        if node not in visited:
            # 인접노드를 스택에 추가
            # stack.append(graph[node])
            # stack.extend(graph[node])          뒤에서부터 방문
            # ['B', 'C', 'D'] => ['D', 'C', 'B']
            # print(list(reversed(graph[node])))
            stack.extend(reversed(graph[node])) #앞에서부터 방문(순서대로)
            visited.append(node)        # 방문처리
            print(f"visited:{visited}")
            print(f"stack:{stack}")
    return visited

print(my_dfs(myGraph, 'A'))
print(my_dfs(myGraph, 'C'))
