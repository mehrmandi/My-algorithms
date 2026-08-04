n, m = [int(x) for x in input().split(" ")]

n = n + 1

edges = []

adj = [[] for _ in range(n)]

graph = [[0 for _ in range(n)] for _ in range(n)]

flag = False


for i in range(m):
    ui, vi, hi = [int(x) for x in input().split(" ")]
    edges.append([ui, vi])
    graph[ui][vi] = hi
    graph[vi][ui] = hi


for edge in edges:
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])


def dfs_rec(adj, g, visited, s, e, h):
    global flag
    visited[s] = True
    # print("e", e)


    for i in adj[s]:

        if i == e and g[s][i] >= h:
            flag = True
        elif g[s][i] >= h and not visited[i]:
            dfs_rec(adj, g, visited, i, e, h)


def dfs(adj, g, u, v, h):
    visited = [False] * len(adj)
    dfs_rec(adj, g, visited, u, v, h)
    if u == v:
        print("Yes")
    elif flag:
        print("YES")
    elif not flag:
        print("NO")



q = int(input())


for i in range(q):
    uj, vj, hj = [int(x) for x in input().split(" ")]
    dfs(adj, graph, uj, vj, hj)
    flag = False

# 5 6
# 1 2 300
# 1 3 700
# 2 4 200
# 2 5 100
# 1 5 300
# 2 3 400
# 4
# 3 5 300
# 3 5 600
# 1 3 200
# 2 4 500

