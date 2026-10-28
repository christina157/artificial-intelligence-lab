# Map Colouring using Constraint Satisfaction Problem (CSP)

colors = ['Red', 'Green', 'Blue']

map_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

coloring = {}

def is_safe(region, color):
    for neighbor in map_graph[region]:
        if coloring.get(neighbor) == color:
            return False
    return True

def solve_csp(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):
            coloring[region] = color

            if solve_csp(regions[1:]):
                return True

            del coloring[region]

    return False

if solve_csp(list(map_graph.keys())):
    print("Map Coloring Solution:")
    for region, color in coloring.items():
        print(region, ":", color)
else:
    print("No solution exists")
