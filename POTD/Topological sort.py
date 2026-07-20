# Topological Sorting vs Depth First Traversal (DFS)(Time Complexity: O(V+E) , Auxiliary Space: O(V))-----------------------

def makeGraph(edges, v):
    graph = [[] for _ in range(v)]

    for edge in edges:
        graph[edge[1]].append(edge[0])

    return graph


def topologicalSortDFS(graph, visited, topological_order, node):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            topologicalSortDFS(graph, visited, topological_order, neighbor)

    topological_order.append(node)

def topologicalSort(edges, v):
    graph = makeGraph(edges, v)
    visited = set()
    topological_order = []
    for node in range(v):
        if node not in visited:
            topologicalSortDFS(graph, visited, topological_order, node)

    return topological_order


V = 4
E = 3
edges = [[3, 0], [1, 0], [2, 0]]
print(topologicalSort(edges, V))

# Kahn’s algorithm for Topological Sorting(Time Complexity: O(V+E) , Auxiliary Space: O(V))---------------------------------------

# from collections import deque
#
#
# # We mainly take input graph as a set of edges. This function is
# # mainly a utility function to convert the edges to an adjacency
# # list
# def constructadj(V, edges):
#     adj = [[] for _ in range(V)]
#     for u, v in edges:
#         adj[u].append(v)
#     return adj
#
#
# # Function to return list containing vertices in Topological order
# def topologicalSort(V, edges):
#     adj = constructadj(V, edges)
#     indegree = [0] * V
#
#     # Calculate indegree of each vertex
#     for u in range(V):
#         for v in adj[u]:
#             indegree[v] += 1
#
#     # Queue to store vertices with indegree 0
#     q = deque([i for i in range(V) if indegree[i] == 0])
#
#     result = []
#     while q:
#         node = q.popleft()
#         result.append(node)
#
#         for neighbor in adj[node]:
#             indegree[neighbor] -= 1
#             if indegree[neighbor] == 0:
#                 q.append(neighbor)
#
#     # Check for cycle
#     if len(result) != V:
#         print("Graph contains cycle!")
#         return []
#
#     return result
#
#
# if __name__ == "__main__":
#     V = 6
#     edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]
#
#     result = topologicalSort(V, edges)
#     if result:
#         print("Topological Order:", result)


