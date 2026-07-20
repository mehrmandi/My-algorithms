def BFS(adj):
    n = len(adj)
    q = []
    res = []
    visited = [False] * n
    q.append(0)
    visited[0] = True

    while len(q) > 0:
        size = len(q)
        for i in range(size):
            curr = q.pop(0)
            res.append(curr)

            for j in adj[curr]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = True

    return res


adj = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
print(BFS(adj))
