import sys
from collections import deque


def solve():
    raw_data = sys.stdin.buffer.read().split()
    if not raw_data:
        return

    n = int(raw_data[0])
    m = int(raw_data[1])

    grid = [raw_data[i + 2].decode("ascii") for i in range(n)]

    d1_id = [[-1] * m for _ in range(n)]
    u_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                if i > 0 and j > 0 and grid[i - 1][j - 1] == ".":
                    d1_id[i][j] = d1_id[i - 1][j - 1]
                else:
                    d1_id[i][j] = u_count
                    u_count += 1

    d2_id = [[-1] * m for _ in range(n)]
    v_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                if i > 0 and j + 1 < m and grid[i - 1][j + 1] == ".":
                    d2_id[i][j] = d2_id[i - 1][j + 1]
                else:
                    d2_id[i][j] = v_count
                    v_count += 1

    adj = [[] for _ in range(u_count)]
    edge_to_cell = {}

    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                u = d1_id[i][j]
                v = d2_id[i][j]
                adj[u].append(v)
                edge_to_cell[(u, v)] = (i + 1, j + 1)

    pair_u = [-1] * u_count
    pair_v = [-1] * v_count
    dist = [-1] * u_count

    def bfs():
        queue = deque()
        for u in range(u_count):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1

        reached_free_v = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                next_u = pair_v[v]
                if next_u != -1:
                    if dist[next_u] == -1:
                        dist[next_u] = dist[u] + 1
                        queue.append(next_u)
                else:
                    reached_free_v = True
        return reached_free_v

    def dfs(u):
        for v in adj[u]:
            next_u = pair_v[v]
            if next_u == -1 or (dist[next_u] == dist[u] + 1 and dfs(next_u)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(u_count):
            if pair_u[u] == -1 and dfs(u):
                matching += 1

    # Output results
    output = [str(matching)]
    for u in range(u_count):
        if pair_u[u] != -1:
            v = pair_u[u]
            r, c = edge_to_cell[(u, v)]
            output.append(f"{r} {c}")

    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solve()
