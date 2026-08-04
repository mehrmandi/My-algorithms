n, m = [int(x) for x in input().split(" ")]

vertex_col = [int(x) for x in input().split(" ")]

adj = [[] for _ in range(n)]

for i in range(m):
    edge = [int(x) for x in input().split(" ")]
    adj[edge[0] - 1]. append(edge[1] - 1)
    adj[edge[1] - 1].append(edge[0] - 1)


def bfs(adj, vc):
    visited = [0 for _ in range(n)]
    q = []
    q.append(0)
    visited[0] = 1
    odd = []
    even = []

    odd.append(0)

    while len(q):
        sz = len(q)

        for i in range(sz):
            curr = q.pop(0)



            for i in range(len(adj[curr])):
                if visited[adj[curr][i]] == 0:
                    q.append(adj[curr][i])
                    visited[adj[curr][i]] = 1
                    if vc[curr] != vc[adj[curr][i]]:
                        if curr in odd:
                            even.append(adj[curr][i])
                        else:
                            odd.append(adj[curr][i])

    return min(len(odd), len(even))




print(bfs(adj, vertex_col))

