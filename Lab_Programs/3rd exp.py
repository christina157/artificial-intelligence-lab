from collections import deque

def water_jug(jug1, jug2, target):
    queue = deque([(0, 0)])
    visited = set()
    parent = {}

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x == target or y == target:
            path = []
            state = (x, y)

            while state != (0, 0):
                path.append(state)
                state = parent[state]

            path.append((0, 0))
            return path[::-1]

        states = [
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (max(0, x - (jug2 - y)), min(jug2, x + y)),
            (min(jug1, x + y), max(0, y - (jug1 - x)))
        ]

        for state in states:
            if state not in visited:
                parent[state] = (x, y)
                queue.append(state)

path = water_jug(4, 3, 2)

for state in path:
    print(state)
