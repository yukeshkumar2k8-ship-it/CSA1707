colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

result = {}

def solve():
    if len(result) == len(graph):
        return True

    region = next(r for r in graph if r not in result)

    for color in colors:
        if all(result.get(n) != color for n in graph[region]):
            result[region] = color
            if solve():
                return True
            del result[region]

    return False

if solve():
    print("Map Coloring Solution:")
    for region, color in result.items():
        print(region, ":", color)
else:
    print("No Solution")
