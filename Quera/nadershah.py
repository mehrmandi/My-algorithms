
import sys

# Increase recursion depth for deep tree traversals
sys.setrecursionlimit(300000)


def solve():
    # Read all tokens from standard input
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    num_test_cases = int(next(iterator))

    output = []

    for _ in range(num_test_cases):
        V = int(next(iterator))  # Number of nodes
        I = int(next(iterator))  # Starting/root node
        A = int(next(iterator))  # Number of branches to pick

        # Node values (1-indexed, so we prepend a dummy 0)
        # Note: input has V values
        values = [0] + [int(next(iterator)) for _ in range(V)]

        adj = [[] for _ in range(V + 1)]
        # A tree with V nodes has V - 1 edges
        for _ in range(V - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)

        # dp[u] stores the maximum path sum going down from node u
        dp = [0] * (V + 1)

        def dfs(u, parent):
            # Base value is the current node's value
            max_child_path = 0
            for child in adj[u]:
                if child != parent:
                    dfs(child, u)
                    if dp[child] > max_child_path:
                        max_child_path = dp[child]
            dp[u] = values[u] + max_child_path

        # Run DFS rooted at starting node I
        dfs(I, 0)

        # Collect the DP values of all immediate children of node I
        branch_values = [dp[child] for child in adj[I]]

        # Sort descending to pick the best A branches
        branch_values.sort(reverse=True)

        # Total diamond value includes the root itself plus top A branches
        total_value = values[I] + sum(branch_values[:A])
        output.append(str(total_value))

    # Print all answers separated by newline
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == '__main__':
    solve()
