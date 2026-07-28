from collections import deque
# import heapq

# # Time Complexity: O((V+E)*logV), Where E is the number of edges and V is the number of vertices.
# # Auxiliary Space: O(V+E)

# # function to construct adjacency list from edges
# def constructAdj(edges, V):
#     adj = [[] for _ in range(V)]

#     for edge in edges:
#         u, v, w = edge
#         adj[u].append([v, w])
#         adj[v].append([u, w])

#     return adj
    
# # Dijkstra's algorithm to find the shortest path from src to dest
# def shortestPath(V: int, src: int, dest: int, edges: list[list[int]]) -> int:
#     adj = constructAdj(edges, V)
#     pq = []
    
#     # Initialize distances to all vertices as infinite
#     dist = [float('inf')] * V
    
#     # Push the source vertex into the priority queue with distance 0
#     heapq.heappush(pq, [0, src])
#     dist[src] = 0
    
#     # Loop until the priority queue is empty
#     while pq:
#         # Pop the vertex with the smallest distance from the priority queue
#         u = heapq.heappop(pq)[1]
    
#         # Loop through all adjacent vertices of the popped vertex
#         for x in adj[u]:
#             v, weight = x[0], x[1]

#             # Update the distance of the adjacent vertex if a shorter path is found
#             if dist[v] > dist[u] + weight:
#                 dist[v] = dist[u] + weight
#                 heapq.heappush(pq, [dist[v], v])
    
#     # Check if the destination vertex is reachable; if not, return -1
#     if dist[dest] == float('inf'):
#         return -1
    
#     return dist[dest]

# Using Edge Splitting Technique with BFS - O(V + E) Time and O(V + E) Space


def shortestPath(V, src, dest, edges):
    extra = V

    # Create adjacency list. Extra nodes
    # are used to split weight 2 edges.
    adj = [[] for _ in range(V + len(edges))]

    for u, v, wt in edges:
        if wt == 1:

            # Weight 1 edge remains unchanged.
            adj[u].append(v)
            adj[v].append(u)
        else:

            # Convert weight 2 edge into two weight 1 edges:
            # u -- 1 -- newNode -- 1 -- v
            adj[u].append(extra)
            adj[extra].append(v)
            adj[v].append(extra)
            adj[extra].append(u)
            extra += 1

    # BFS on the transformed unweighted
    # graph gives shortest distance.
    dist = [-1] * extra
    dist[src] = 0
    q = deque([src])

    while q:
        node = q.popleft()
        if node == dest:
            return dist[node]
        for nxt in adj[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                q.append(nxt)

    # Destination is not reachable from source.
    return -1


    
V = 5
edges = [[0, 1, 1], [0, 2, 2], [1, 2, 1], [3, 4, 2]]
src = 1
dest = 3
print(shortestPath(V, src, dest, edges))


