from collections import defaultdict

def add_edge(edges):
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph

def dfs(u, graph, parent, visited, disc, low, bridges, time):
    visited[u] = True
    disc[u] = time[0]
    low[u] = time[0]
    time[0] += 1
    
    for v in graph[u]:
        if not visited[v]:
            parent[v] = u
            dfs(v, graph, parent, visited, disc, low, bridges, time)

            low[u] = min(low[u], low[v])

            if low[v] > disc[u]:
                bridges.append((u, v))
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])



def bridgeFind(edges, V):
    graph = add_edge(edges)
    visited = [False] * V
    disc = [float("inf")] * V
    low = [float("inf")] * V
    parent = [-1] * V
    time = [0]
    bridges = []

    for i in range(V):
        if not visited[i]:
            dfs(i, graph, parent, visited, disc, low, bridges, time)

    return bridges

def isBridge(edges, c, d, V):
    bridges = bridgeFind(edges, V)

    if (c, d) in bridges or (d, c) in bridges:
        return True
    else:
        return False


V = 5
c = 1
d = 2
edges = [[0, 1], [1, 2], [2, 3]]
print(isBridge(edges, c, d, V))


# Approach: Using DFS - O(V + E) Time and O(V) Space---------------------------


def dfs(adj, c, visited):
    # Standard DFS traversal from node c
    visited[c] = True
    for neighbor in adj[c]:
        if not visited[neighbor]:
            dfs(adj, neighbor, visited)


def constructadj(V, edges, c, d):
    # Build adjacency list, skipping the edge (c, d)
    adj = [[] for _ in range(V)]
    for a, b in edges:

        # Skip the edge we're testing as a potential bridge
        if (a == c and b == d) or (a == d and b == c):
            continue
        adj[a].append(b)
        adj[b].append(a)
    return adj


def isBridge(V, edges, c, d):
    # Build the graph without edge (c, d)
    adj = constructadj(V, edges, c, d)
    visited = [False] * V

    # Run DFS starting from one end of the removed edge
    dfs(adj, c, visited)

    # If we can't reach the other node, it's a bridge
    return not visited[d]


if __name__ == "__main__":
    # Number of vertices
    V = 4

    # Edges of the graph
    edges = [[0, 1], [1, 2], [2, 3]]

    # Edge we want to test
    c, d = 1, 2
    # Output true if the edge is a bridge, false otherwise
    print("true" if isBridge(V, edges, c, d) else "false")