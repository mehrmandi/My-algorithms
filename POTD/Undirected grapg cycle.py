def dfs(v, visited, parent, graph):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if dfs(neighbor, visited, v, graph):
                return True
        elif neighbor != parent:
            return True
    return False

def detectCycle(edges, V):
    graph = {i: [] for i in range(V)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            if dfs(i, visited, -1, graph):
                return True
    return False


V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
print(detectCycle(edges, V))