from collections import deque

GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

def get_neighbors(state):
    neighbors = []

    # Find the blank tile (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]

            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y]
            )

            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == GOAL:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))

    return None


start = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

solution = bfs(start)

if solution:
    print("Solution Found!")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
