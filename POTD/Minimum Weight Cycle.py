# from collections import defaultdict
# import sys


# def find_minimum_cycle(V, edges):
#     graph = defaultdict(list)

#     # Build adjacency list for the graph
#     for u, v, w in edges:
#         graph[u].append((v, w))
#         graph[v].append((u, w))

#     def dfs(node, visited, parent, start_node, weight):
#         nonlocal min_cycle_weight

#         visited[node] = True

#         for neighbor, edge_weight in graph[node]:
#             if neighbor == parent:  # Ignore the edge leading back to the parent
#                 continue
#             if visited[neighbor]:
#                 # A cycle is found if the neighbor is the start node
#                 if neighbor == start_node:
#                     min_cycle_weight = min(min_cycle_weight, weight + edge_weight)
#             else:
#                 # Visit the neighbor
#                 dfs(neighbor, visited, node, start_node, weight + edge_weight)

#         visited[node] = False  # Backtracking

#     min_cycle_weight = sys.maxsize

#     # Try to find cycles starting from each node
#     for i in range(V):
#         visited = [False] * V
#         dfs(i, visited, -1, i, 0)

#     return (
#         min_cycle_weight if min_cycle_weight != sys.maxsize else -1
#     )  # Return -1 if no cycle exists


# # Example usage
# V = 5
# edges = [[0, 1, 3], [1, 2, 2], [0, 4, 1], [1, 4, 2], [1, 3, 1], [3, 4, 2], [2, 3, 3]]

# print(find_minimum_cycle(V, edges))


# better time complexity ----------------------------------------------------------------------
import heapq
from collections import defaultdict


def find_min_cycle(V, edges):
    # Build graph as adjacency list
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # undirected

    def dijkstra(start, banned_u, banned_v):
        dist = [float("inf")] * V
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                # Skip the banned edge
                if (node == banned_u and neighbor == banned_v) or (
                    node == banned_v and neighbor == banned_u
                ):
                    continue
                if dist[neighbor] > d + weight:
                    dist[neighbor] = d + weight
                    heapq.heappush(pq, (dist[neighbor], neighbor))
        return dist

    min_cycle = float("inf")

    for u, v, w in edges:
        # Temporarily remove edge u-v by skipping it in Dijkstra
        dist = dijkstra(u, u, v)
        if dist[v] != float("inf"):
            min_cycle = min(min_cycle, dist[v] + w)

    return min_cycle if min_cycle != float("inf") else -1



V = 5
edges = [[0, 1, 2], [1, 2, 2], [1, 3, 1], [1, 4, 1], [0, 4, 3], [2, 3, 4]]
print(find_min_cycle(V, edges))
