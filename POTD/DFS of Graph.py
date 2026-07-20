def dfs_rec(visited, dfs_list, s):
    visited[s] = True
    dfs_list.append(s)

    for i in adj[s]:
        if not visited[i]:
            dfs_rec(visited, dfs_list, i)


def dfs(adj):
    visited = [False] * len(adj)
    dfs_list = []

    for i in range(len(adj)):
        if not visited[i]:
            dfs_rec(visited, dfs_list, i)

    return dfs_list


adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(dfs(adj))