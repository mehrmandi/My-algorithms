sherlok = int(input())
v = int(input()) + 1
line = int(input())
edges = []
graph = [[] for _ in range(v)]
cycles = [[] for i in range(v)]
color = [0] * v
par = [0] * v
cyclenumber = 0
shortest_path = [0] * 9999

for i in range(line):
    edge = [int(x) for x in input().split(" ")]
    edges.append(edge)

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

def dfs_cycle(u, p, color: list,
              par: list):
    global cyclenumber

    if color[u] == 2:
        return

    if color[u] == 1:
        q = []
        cur = p
        q.append(cur)

        while cur != u:
            cur = par[cur]
            q.append(cur)
        cycles[cyclenumber] = q
        cyclenumber += 1

        return

    par[u] = p

    color[u] = 1

    for v in graph[u]:

        if v == par[u]:
            continue
        dfs_cycle(v, u, color, par)

    color[u] = 2




dfs_cycle(1, 0, color, par)


def bfs(graph, s, par, dist):
    q = []
    dist[s] = 0
    q.append(s)
    while q:
        node = q.pop(0)
        for neighbor in graph[node]:
            if dist[neighbor] == float('inf'):
                par[neighbor] = node
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)


def shortest_distance(graph, S, D, V):
    global shortest_path
    par = [-1] * V
    dist = [float('inf')] * V
    bfs(graph, S, par, dist)

    path = []
    current_node = D
    path.append(D)
    while par[current_node] != -1:
        path.append(par[current_node])
        current_node = par[current_node]

    path.reverse()
    if len(path) < len(shortest_path):
        shortest_path = path


for i in range(0, cyclenumber):
    for D in cycles[i]:
        shortest_distance(graph, sherlok, D, v)


for x in shortest_path:
    print(x, end=" ")