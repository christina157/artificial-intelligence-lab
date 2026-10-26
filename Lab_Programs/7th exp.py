def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=" ")
        visited.add(start)

        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS Traversal:")
dfs(graph, 'A')
