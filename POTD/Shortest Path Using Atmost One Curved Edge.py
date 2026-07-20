import heapq
# [Approach 1] Using Dijkstra with State Compression - O((V+E) log V) Time and O(V+E) Space------------------
def shortestPath(V, a, b, edges):
    adj = [[] for _ in range(V)]
    
    for edge in edges:
        adj[edge[0]].append([edge[1], edge[2], edge[3]])
        adj[edge[1]].append([edge[0], edge[2], edge[3]])

    print(adj)
    INF = float('inf')
    dist = [[INF , INF] for _ in range(V)]
    dist[a][0] = 0
    
    pq = []
    heapq.heappush(pq, [0, a, 0])
    
    while pq:
        print("pq", pq)
        d, v, used = heapq.heappop(pq)
        
        print("d, v, used", d, v, used)
        
        if d > dist[v][used]:
            continue
        
        for u, w1, w2 in adj[v]:
            print("u, w1, w2", u, w1, w2)
            if d + w1 < dist[u][used]:
                print("1111111111111111")
                dist[u][used] = d + w1
                heapq.heappush(pq, [dist[u][used], u, used])
                
                
            if used == 0 and d + w2 < dist[u][1]:
                print("222222222222222")
                dist[u][1] = d + w2
                heapq.heappush(pq, [dist[u][1], u, 1])
            print("dist", dist)        
    ans = min(dist[b][0], dist[b][1])
    
    return ans if ans != float('inf') else -1
  
    
    
V = 4
E = 4
a = 1
b = 3
edges = [[0, 1, 1, 4], [0, 2, 2, 4], [0, 3, 3, 1], [1, 3, 6, 5]]
print(shortestPath(V, a, b, edges))

# [Approach 2] Using Two-Dijkstra Method with Curved-Edge Relaxation - O((V+E) log V) Time and O(V+E) Space----------------


# def dijkstra(src, n, adj):

#     # Distance array initialized with INF
#     dist = [10**9] * n

#     # Min-heap priority queue: (distance_so_far, node)
#     pq = []

#     dist[src] = 0
#     heapq.heappush(pq, (0, src))

#     while pq:
#         d, u = heapq.heappop(pq)

#         # Explore all neighbors of u
#         for v, straight, curved in adj[u]:

#             # Relaxation step
#             if dist[v] > d + straight:
#                 dist[v] = d + straight
#                 heapq.heappush(pq, (dist[v], v))

#     return dist


# # Function to find shortest path from a to b using at most one curved edge
# def shortestPath(a, b, adj):
#     n = len(adj)

#     # Shortest distances using only straight edges
#     # from source and destination
#     da = dijkstra(a, n, adj)
#     db = dijkstra(b, n, adj)

#     ans = da[b]

#     # Check all curved edges to see if using one improves the answer
#     for u in range(n):
#         for v, straight, curved in adj[u]:

#             # Two possible paths using the curved edge
#             ans = min(ans, da[u] + curved + db[v])
#             ans = min(ans, da[v] + curved + db[u])

#     if ans >= 10**9:
#         return -1

#     return ans


# if __name__ == "__main__":
#     a = 1
#     b = 3

#     adj = [
#         [(1, 1, 4), (2, 2, 4), (3, 3, 1)],
#         [(0, 1, 4), (3, 6, 5)],
#         [(0, 2, 4)],
#         [(0, 3, 1), (1, 6, 5)]
#     ]

#     print(shortestPath(a, b, adj))
