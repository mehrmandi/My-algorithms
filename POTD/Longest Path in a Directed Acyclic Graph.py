# Given a weighted Directed Acyclic Graph(DAG) with V vertices numbered from 0 to V - 1, represented by edges[][], where edges[i] = [u, v, w] denotes a directed edge from u to v with weight w, and a source vertex src.

# Return the distance array, where the value at index i represents the longest distance from s to vertex i.
# If a vertex is unreachable from s, store INT_MIN for that vertex. The driver code will automatically display INT_MIN as INF.

# Time Complexity: O(V + E)
# Auxiliary Space: O(V)


from collections import deque

def maxDistance(V, src, edges):
    g = [[] for _ in range(V)]
    indegree = [0] * V

    for u, v, wt in edges:
        g[u].append((v, wt))
        indegree[v] += 1

    # Topological sort
    q = deque()

    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    topoOrder = []

    while q:
        node = q.popleft()
        topoOrder.append(node)

        for v, wt in g[node]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    INT_MIN = -(2 ** 31)
    dist = [INT_MIN] * V
    dist[src] = 0

    # Longest path in DAG
    for node in topoOrder:
        if dist[node] == INT_MIN:
            continue

        for v, wt in g[node]:
            dist[v] = max(dist[v], dist[node] + wt)

    return dist


V = 5
src = 1
edges = [[0, 1, 1], [0, 2, 2], [1, 4, 4], [3, 2, -1], [4, 2, 3], [4, 3, 6]]
print(maxDistance(V, src, edges))  # Output: 2
