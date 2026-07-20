def makeAdj(edges, V):
    adj = [[] for _ in range(V)]

    for edge in edges:
        adj[edge[0]].append(edge[1])

    return adj

def dfs_rec(visited, adj, s):

    visited[s] = "G"
    for i in adj[s]:
        if visited[i] == "G":
            return True

        if visited[i] == "W" and dfs_rec(visited, adj, i):
            return True

    visited[s] = "B"
    return False



def isCycle(edges, V):
    visited = ["W"] * V
    adj = makeAdj(edges, V)

    for i in range(V):
        if visited[i] == "W":
            if dfs_rec(visited, adj, i):
                print(visited)
                return True
    print(visited)
    return False

V = 6
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [3, 4], [4, 5]]
print(isCycle(edges, V))


# Using DFS - O(V + E) Time and O(V) Space----------------------------
# Helper function for DFS-based cycle detection
# def isCyclicUtil(adj, u, visited, recStack):
#     # If the node is already in the current recursion stack, a cycle is detected
#     if recStack[u]:
#         return True
#
#     # If the node is already visited and not part of the recursion stack, skip it
#     if visited[u]:
#         return False
#
#     # Mark the current node as visited and add it to the recursion stack
#     visited[u] = True
#     recStack[u] = True
#
#     # Recur for all the adjacent vertices
#     for v in adj[u]:
#         if isCyclicUtil(adj, v, visited, recStack):
#             return True
#
#     # Remove the node from the recursion stack before returning
#     recStack[u] = False
#     return False
#
# # Function to build adjacency list from edge list
#
#
# def constructadj(V, edges):
#     adj = [[] for _ in range(V)]  # Create a list for each vertex
#     for u, v in edges:
#         adj[u].append(v)  # Add directed edge from u to v
#     return adj
#
# # Main function to detect cycle in the directed graph
#
#
# def isCyclic(V, edges):
#     adj = constructadj(V, edges)
#     visited = [False] * V       # To track visited vertices
#     recStack = [False] * V      # To track vertices in the current DFS path
#
#     # Try DFS from each vertex
#     for i in range(V):
#         if not visited[i] and isCyclicUtil(adj, i, visited, recStack):
#             return True  # Cycle found
#     return False  # No cycle found
#
#
# # Example usage
# V = 4  # Number of vertices
# edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
#
# # Output: True, because there is a cycle (0 → 2 → 0)
# print(isCyclic(V, edges))


# Using Topological Sorting - O(V + E) Time and O(V) Space-----------------------------
# from collections import deque
#
# # Function to construct adjacency list from edge list
#
#
# def constructadj(V, edges):
#     adj = [[] for _ in range(V)]  # Initialize empty list for each vertex
#     for u, v in edges:
#         adj[u].append(v)          # Directed edge from u to v
#     return adj
#
# # Function to check for cycle using Kahn's Algorithm (BFS-based Topological Sort)
#
#
# def isCyclic(V, edges):
#     adj = constructadj(V, edges)
#     in_degree = [0] * V
#     queue = deque()
#     visited = 0                       # Count of visited nodes
#
#     #  Calculate in-degree of each node
#     for u in range(V):
#         for v in adj[u]:
#             in_degree[v] += 1
#
#     #  Enqueue nodes with in-degree 0
#     for u in range(V):
#         if in_degree[u] == 0:
#             queue.append(u)
#
#     #  Perform BFS (Topological Sort)
#     while queue:
#         u = queue.popleft()
#         visited += 1
#
#         # Decrease in-degree of adjacent nodes
#         for v in adj[u]:
#             in_degree[v] -= 1
#             if in_degree[v] == 0:
#                 queue.append(v)
#
#     #  If visited != V, graph has a cycle
#     return visited != V
#
#
# # Example usage
# V = 4
# edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]
#
# # Output: true (because there is a cycle: 0 → 2 → 0)
# print("true" if isCyclic(V, edges) else "false")