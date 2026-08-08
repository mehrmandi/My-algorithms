# Given a graph with n vertices (0 to n-1) and m edges. You can remove one edge from anywhere and add that edge between any two vertices in one operation.

# Find the minimum number of operations required to connect the graph. If it is not possible to connect the graph, return -1.

# function to perform DFS traversal of the graph
def dfs(adj, visited, node):
    visited[node] = True
    
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(adj, visited, neighbor)
    


def minEdgesReq(n, edges):
    m = len(edges)
    # If the number of edges is less than n - 1, it is impossible to connect the graph
    if m < n - 1:
        return -1
    
    # Count the number of connected components in the graph
    res = 0
    visited = [False for _ in range(n)]
    adj = [[] for _ in range(n)]
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    for node in range(n):
        if not visited[node]:
            res += 1
            dfs(adj, visited, node)
            
    return res - 1
            

n = 4
edges = [[0, 1], [0, 2], [1, 2]]
print(minEdgesReq(n, edges))