# Time Complexity: O(V+E), Using DFS to explore all paths, each node is visited atmost once.----------------------------------
# Auxiliary Space: O(V), Using boolean Visited and safe state arrays.

# # Checks if the given node is safe or part of a cycle
# def dfs(curNode, visited, safe, adj):
#     # Mark current node as visited
#     visited[curNode] = True

#     # Assume the node is safe until proven otherwise
#     isSafe = True

#     # Exploring all paths
#     for nextNode in adj[curNode]:
#         if not visited[nextNode]:
#             isSafe &= dfs(nextNode, visited, safe, adj)
#         # If the adjacent node is already visited and not safe,
#         # it means the current node is part of a cycle
#         elif not safe[nextNode]:
#             isSafe = False
#             break

#     # Update and return if curNode
#     # is safe node or not.
#     safe[curNode] = isSafe
#     return isSafe


# def safeNodes(adj):
#     v = len(adj)
#     ans = []
#     visited = [False] * v
#     safe = [False] * v

#     # Perform DFS for each unvisited node
#     for i in range(v):
#         if not visited[i]:
#             dfs(i, visited, safe, adj)

#     # Collect all safe nodes
#     for i in range(v):
#         if safe[i]:
#             ans.append(i)

#     return ans


# def addEdge(adj, u, v):
#     adj[u].append(v)


# if __name__ == "__main__":
#     n = 5
#     adj = [[] for _ in range(n)]

#     # creating adjacency list
#     addEdge(adj, 1, 0)
#     addEdge(adj, 1, 2)
#     addEdge(adj, 1, 3)
#     addEdge(adj, 1, 4)
#     addEdge(adj, 2, 3)
#     addEdge(adj, 3, 4)

#     res = safeNodes(adj)

#     for vertex in res:
#         print(vertex, end=" ")
#     print()


from collections import deque


def addEdge(adj, u, v):
    adj[u].append(v)

def safeNodes(V, edges):
    adj = [[] for _ in range(V)]
    
    for edge in edges:
        addEdge(adj, edge[0], edge[1])
    
    revAdj = [[] for _ in range(V)]
    indegree = [0] * V

    # Build reversed adjacency list
    # and compute indegree for each node
    for i in range(V):
        for nextNode in adj[i]:
            revAdj[nextNode].append(i)
            indegree[i] += 1

    q = deque()
    ans = []

    # Push all terminal nodes
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    # Kahn's Algo on reversed graph
    while q:
        curNode = q.popleft()
        ans.append(curNode)

        for prevNode in revAdj[curNode]:
            indegree[prevNode] -= 1
            if indegree[prevNode] == 0:
                q.append(prevNode)

    # Return safe nodes
    return ans


V = 5
E = 6
edges = [[1, 0], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
print(safeNodes(V, edges))






