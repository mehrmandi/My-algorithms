import heapq
import sys
def countPaths(V, edges):
    adj = [[] for _ in range(V)]
    
    for edge in edges:
        u, v, w = edge
        adj[u].append([v, w])
        adj[v].append([u, w])
        
    print(adj)
    
    src = 0
    res = 0

    # Min-heap (priority queue) storing pairs of (distance, node)
    pq = []

    dist = [sys.maxsize] * V
    same_short_path = [0] * V
    
    same_short_path[0] = 1

    # Distance from source to itself is 0
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    # Process the queue until all reachable vertices are finalized
    while pq:
        d, u = heapq.heappop(pq)

        # If this distance not the latest shortest one, skip it
        if d > dist[u]:
            continue

        # Explore all neighbors of the current vertex
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                same_short_path[v] = same_short_path[u]
                
            elif dist[u] + w == dist[v]:
                same_short_path[v] = same_short_path[v] + same_short_path[u]
                
            # If we found a shorter path to v through u, update it
            

    # Return the final shortest distances from the source
    return same_short_path[V - 1]


V = 6
edges = [[0, 2, 3], [0, 4, 2], [0, 5, 7], [2, 3, 1], [
    2, 5, 5], [5, 3, 3], [5, 1, 4], [1, 4, 1], [4, 5, 5]]
print(countPaths(V, edges))