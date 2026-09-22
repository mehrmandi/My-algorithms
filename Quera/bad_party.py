import sys
import os

# --- LOCAL TESTING SETUP ---
# Reads from input.txt if present locally, otherwise reads from standard input
DEBUG = os.path.exists("input.txt")
if DEBUG:
    sys.stdin = open("input.txt", "r")
# ---------------------------


def guest():
    # Increase recursion depth for deep trees if needed
    sys.setrecursionlimit(500000)

    # Read all tokens at once
    input_data = sys.stdin.read().split() if DEBUG else sys.stdin.buffer.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))

    # We only need enough capacity up to the max node value or standard constraint
    MAX_NODES = 300005
    parent = list(range(MAX_NODES))
    rank = [0] * MAX_NODES

    def find(x):
        # Path compression (iterative or standard recursive)
        root = x
        while root != parent[root]:
            root = parent[root]

        curr = x
        while curr != root:
            nxt = parent[curr]
            parent[curr] = root
            curr = nxt
        return root

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return

        # Union by rank to keep the tree flat
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Keep track of active vertices present in the input
    active_nodes = set()

    for _ in range(n):
        u = int(next(it))
        v = int(next(it))
        union(u, v)
        active_nodes.add(u)
        active_nodes.add(v)

    if not active_nodes:
        print(0)
        return

    # Count distinct component leaders among all active nodes
    components = {find(node) for node in active_nodes}

    # Minimum additional edges needed to connect all components
    ans = len(components) - 1
    sys.stdout.write(str(ans) + "\n")


if __name__ == "__main__":
    guest()
