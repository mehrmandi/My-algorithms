def findArticulationPoints(V, edges):
    # Step 1: Build the adjacency list
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Initialize variables
    disc = [-1] * V
    low = [-1] * V
    parent = [-1] * V
    visited = [False] * V
    ap = [False] * V
    time = [0]

    def dfs(u):
        # Count of children in DFS tree
        children = 0
        visited[u] = True
        disc[u] = low[u] = time[0]
        time[0] += 1

        # Explore all the neighbors of u
        for v in adj[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                # Recur for DFS traversal
                dfs(v)

                # After recursion, update the low time of u
                low[u] = min(low[u], low[v])

                # (1) u is root and has more than one child, it's an articulation point
                if parent[u] == -1 and children > 1:
                    ap[u] = True

                # (2) u is not root and low[v] >= disc[u], it's an articulation point
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:  # Update low[u] for back edge
                low[u] = min(low[u], disc[v])

    # Call the DFS function for all unvisited vertices
    for i in range(V):
        if not visited[i]:
            dfs(i)

    # Collect all articulation points
    result = [i for i in range(V) if ap[i]]
    if not result:
        return [-1]
    else:
        return result

# Example usage:
V = 2
edges = [[0, 1]]
articulation_points = findArticulationPoints(V, edges)
print("Articulation Points:", articulation_points)


# [Expected Approach] Using Tarjan's Algorithm - O(V + E) Time and O(V) Space------------------
# def constructAdj(V, edges):
#     adj = [[] for _ in range(V)]
#
#     for edge in edges:
#         adj[edge[0]].append(edge[1])
#         adj[edge[1]].append(edge[0])
#     return adj
#
#
# # Helper function to perform DFS and find articulation points
# # using Tarjan's algorithm.
# def findPoints(adj, u, visited, disc, low, time, parent, isAP):
#     # Mark vertex u as visited and assign discovery
#     # time and low value
#     visited[u] = 1
#     time[0] += 1
#     disc[u] = low[u] = time[0]
#     children = 0
#
#     # Process all adjacent vertices of u
#     for v in adj[u]:
#
#         # If v is not visited, then recursively visit it
#         if not visited[v]:
#             children += 1
#             findPoints(adj, v, visited, disc, low, time, u, isAP)
#
#             # Check if the subtree rooted at v has a
#             # connection to one of the ancestors of u
#             low[u] = min(low[u], low[v])
#
#             # If u is not a root and low[v] is greater than or equal to disc[u],
#             # then u is an articulation point
#             if parent != -1 and low[v] >= disc[u]:
#                 isAP[u] = 1
#
#         # Update low value of u for back edge
#         elif v != parent:
#             low[u] = min(low[u], disc[v])
#
#     # If u is root of DFS tree and has more than
#     # one child, it is an articulation point
#     if parent == -1 and children > 1:
#         isAP[u] = 1
#
#
# # Main function to find articulation points in the graph
# def articulationPoints(V, edges):
#     adj = constructAdj(V, edges)
#     disc = [0] * V
#     low = [0] * V
#     visited = [0] * V
#     isAP = [0] * V
#     time = [0]
#
#     # Run DFS from each vertex if not
#     # already visited (to handle disconnected graphs)
#     for u in range(V):
#         if not visited[u]:
#             findPoints(adj, u, visited, disc, low, time, -1, isAP)
#
#     # Collect all vertices that are articulation points
#     result = [u for u in range(V) if isAP[u]]
#
#     # If no articulation points are found, return list containing -1
#     return result if result else [-1]
#
#
# if __name__ == "__main__":
#     V = 5
#     edges = [[0, 1], [1, 4], [2, 3], [2, 4], [3, 4]]
#     ans = articulationPoints(V, edges)
#
#     for u in ans:
#         print(u, end=' ')
#     print()


# [Naive Approach] Using DFS - O(V * (V + E)) Time and O(V) Space------------------
# Python program to find articulation points using a naive DFS approach

# def dfs(node, adj, visited):
#     # Standard DFS to mark all reachable nodes
#     visited[node] = True
#
#     for neighbor in adj[node]:
#         if not visited[neighbor]:
#             dfs(neighbor, adj, visited)
#
#
# def constructadj(V, edges):
#     # Builds adjacency list from edge list
#     adj = [[] for _ in range(V)]
#     for u, v in edges:
#         adj[u].append(v)
#         adj[v].append(u)
#     return adj
#
#
# def articulationPoints(V, edges):
#     # Finds articulation points using naive DFS approach
#     adj = constructadj(V, edges)
#     res = []
#
#     # Try removing each node one by one
#     for i in range(V):
#         visited = [False] * V
#         visited[i] = True
#
#         # count DFS calls from i's neighbors
#         comp = 0
#         for it in adj[i]:
#             if comp > 1:
#                 break
#             if not visited[it]:
#                 # explore connected part
#                 dfs(it, adj, visited)
#                 comp += 1
#
#         # if more than one component forms, it's an articulation point
#         if comp > 1:
#             res.append(i)
#
#     if not res:
#         return [-1]
#
#     return res
#
#
# if __name__ == "__main__":
#     V = 5
#     edges = [[0, 1], [1, 4], [2, 3], [2, 4], [3, 4]]
#
#     ans = articulationPoints(V, edges)
#     for it in ans:
#         print(it, end=" ")
