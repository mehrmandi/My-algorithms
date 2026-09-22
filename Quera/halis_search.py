import sys
from collections import deque


def solve():
    # Read all tokens from standard input using fast I/O
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    k = int(next(iterator))  # Sherlock's starting city
    n = int(next(iterator))  # Number of cities (vertices)
    m = int(next(iterator))  # Number of roads (edges)

    # 1-indexed adjacency list and degree array
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)

    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Step 1: Iteratively prune leaf nodes (degree <= 1) to find cycle vertices
    # Any node belonging to a simple cycle has degree >= 2 and cannot be pruned.
    deg = list(degree)
    queue = deque([i for i in range(1, n + 1) if deg[i] <= 1])
    is_cycle_node = [True] * (n + 1)

    while queue:
        curr = queue.popleft()
        is_cycle_node[curr] = False
        for neighbor in adj[curr]:
            if is_cycle_node[neighbor]:
                deg[neighbor] -= 1
                if deg[neighbor] <= 1:
                    queue.append(neighbor)

    # Step 2: BFS starting from Sherlock's city (k) to find the shortest path
    # to the first cycle node encountered.
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)

    bfs_queue = deque([k])
    visited[k] = True
    target_node = -1

    while bfs_queue:
        curr = bfs_queue.popleft()

        # If we reached a node that belongs to a cycle, stop
        if is_cycle_node[curr]:
            target_node = curr
            break

        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = curr
                bfs_queue.append(neighbor)

    # Step 3: Reconstruct the path from k to target_node
    path = []
    curr = target_node
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    # Print the resulting path
    print(*(path))


if __name__ == '__main__':
    solve()
