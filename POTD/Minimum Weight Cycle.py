# Given an undirected weighted graph represented by an adjacency list adj[][][], where adj[u][i] = [v, w] represents an edge between vertices u and v with weight w.

# Find the minimum weight cycle in the graph and return its total weight.

# Note: The graph is guaranteed to contain at least one cycle.

# Dijkstra's algorithm - O(E * (V + E) log V) Time and O(V+E) Space

import heapq

# Find shortest path between src and dest


def shortestPath(V, adj, src, dest):
    dist = [float('inf')] * V
    dist[src] = 0

    # Priority queue
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for neighbor in adj[u]:
            v = neighbor[0]
            w = neighbor[1]

            # Skip the ignored edge
            if (u == src and v == dest) or \
               (u == dest and v == src):
                continue

            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist[dest]


# Function to find the minimum weight cycle
def findMinCycle(adj):
    V = len(adj)
    minCycle = float('inf')

    for u in range(V):
        for edge in adj[u]:
            v = edge[0]
            w = edge[1]

            # Process each undirected edge only once
            if u < v:
                dist = shortestPath(V, adj, u, v)

                if dist != float('inf'):
                    minCycle = min(minCycle, dist + w)

    return minCycle


if __name__ == "__main__":
    adj = [[] for _ in range(5)]

    adj[0] = [[1, 2], [4, 3]]
    adj[1] = [[0, 2], [2, 2], [3, 1], [4, 1]]
    adj[2] = [[1, 2], [3, 4]]
    adj[3] = [[1, 1], [2, 4]]
    adj[4] = [[1, 1], [0, 3]]

    result = findMinCycle(adj)
    print(result)
