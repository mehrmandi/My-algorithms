# Given an undirected graph(with no cycles) represented using an adjacency list adj[][], find the diameter of the graph.
# The diameter of a graph(sometimes called the width) is the number of edges on the longest path between two nodes in the graph.

# Note: Graph do not contain any disconnected component.

# Finding ends of diameter - O(n) Time and O(n) Space

def farthestNode(curr, visited, adj, dist):
    if visited[curr]:
        return 0

    visited[curr] = True
    maxDist = dist

    for next_node in adj[curr]:
        # visiting the next node
        # if not visited already
        if not visited[next_node]:
            maxDist = max(maxDist, farthestNode(
                next_node, visited, adj, dist + 1))
    return maxDist


def diameter(adj):
    n = len(adj)
    res = 0

    # taking maximum across all nodes
    for i in range(n):
        visited = [False] * n
        res = max(res, farthestNode(i, visited, adj, 0))
    return res

# Driver Code Starts


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

          
adj = [[1], [0, 2], [1, 3], [2, 4], [3]]
print(diameter(V, edges))
