def astar(graph, start, goal, h):
    open_list = [(start, 0)]
    g_cost = {start: 0}
    parent = {}

    while open_list:
        open_list.sort(key=lambda x: x[1] + h[x[0]])
        current, _ = open_list.pop(0)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            print("Shortest Path:", path[::-1])
            print("Total Cost:", g_cost[goal])
            return

        for neighbor, cost in graph[current].items():
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                parent[neighbor] = current
                open_list.append((neighbor, new_cost))

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 4},
    'E': {'G': 2},
    'F': {'G': 3},
    'G': {}
}

h = {'A': 6, 'B': 5, 'C': 4, 'D': 4, 'E': 2, 'F': 3, 'G': 0}

astar(graph, 'A', 'G', h)
