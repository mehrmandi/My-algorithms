import heapq
import sys

# Time Complexity: O((V+E)*logV), Where E is the number of edges and V is the number of vertices.
# Auxiliary Space: O(V+E)

def constructAdj(edges, V):
    adj = [[] for _ in range(V)]

    for edge in edges:
        u, v, wt = edge
        adj[u].append([v, wt])
        adj[v].append([u, wt])

    return adj


def dijkstra(V, edges, src):
    adj = constructAdj(edges, V)

    pq = []

    dist = [sys.maxsize] * V

    heapq.heappush(pq, [0, src])
    dist[src] = 0

    while pq:
        u = heapq.heappop(pq)[1]

        for x in adj[u]:
            v, weight = x[0], x[1]

            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, [dist[v], v])

    return dist



V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2
print(dijkstra(V, edges, src))