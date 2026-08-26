# Using Bellman–Ford - O(V * E) and O(V) Space

def isNegativeWeightCycle(V: int, edges: list[list[int]]) -> bool:
    dist = [0] * V

    for i in range(V):
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

                # Update on the V-th iteration => negative cycle
                if i == V - 1:
                    return True

    return False


V = 4
edges = [[0, 3, 6], [1, 0, 4], [1, 2, 6], [3, 1, 2]]
print(isNegativeWeightCycle(V, edges))
