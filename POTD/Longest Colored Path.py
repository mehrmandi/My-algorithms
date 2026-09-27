# Given an undirected acyclic graph(tree) with n nodes numbered from 1 to n. Each node is colored either Red(R) or Blue(B).

# The colors of the nodes are given by a string s of length n, where:

# s[i] = 'R' means node i + 1 is Red.
# s[i] = 'B' means node i + 1 is Blue.
# You are also given a list of n - 1 edges edges[][], where each edges[i] = [u, v] represents an undirected edge between nodes u and v.

# You can start from any node and traverse along the edges to form a path.

# A path is called valid if , once you visit a Blue node, you cannot visit any Red node after it on the same path.

# In other words, a valid path must have the following form:

# Only Red nodes, or
# Only Blue nodes, or
# Some Red nodes followed by some Blue nodes.
# A path containing a pattern like Blue -> Red is invalid.
# Find the maximum number of nodes in a valid path.

# Using Tree DP with Rerooting - O(n) Time and O(n) Space


# Perform a bottom-up DFS to calculate the best path
# contribution coming from each node's subtree.
def root(adj, s, sa, node=0, par=-1):
    ra = 0
    ba = 0

    # Process all children of the current node.
    for it in adj[node]:
        if it == par:
            continue

        # Calculate DP values for the child subtree.
        root(adj, s, sa, it, node)

        # Store the maximum possible contribution
        # for a path ending at a Red node.
        ra = max(ra, sa[it][0])
        ra = max(ra, sa[it][1])

        # Store the maximum possible contribution
        # for a path ending at a Blue node.
        ba = max(ba, sa[it][1])

    # Calculate the DP values based on the
    # color of the current node.
    if s[node] == 'R':
        sa[node][0] = ra + 1
        sa[node][1] = 0
    else:
        sa[node][0] = ba + 1
        sa[node][1] = ba + 1


# Reroot the tree to include contributions
# coming from the parent and sibling subtrees.
def reroot(adj, s, ans, sa, node=0, par=-1, red_par=0, blue_par=0):
    # Calculate the best answer for the current node
    # by considering both subtree and parent contributions.
    if s[node] == 'R':
        ans[node][0] = max(sa[node][0], 1 + red_par)
        ans[node][1] = 0
    else:
        ans[node][0] = max(sa[node][0], 1 + blue_par)
        ans[node][1] = max(sa[node][1], 1 + blue_par)

    # Find the largest and second-largest contributions
    # from all child subtrees.
    fr = red_par
    sr = red_par
    fb = blue_par
    sb = blue_par

    for it in adj[node]:
        if it == par:
            continue

        # Maintain the two largest Red contributions.
        if sa[it][0] > fr:
            sr = fr
            fr = sa[it][0]
        elif sa[it][0] > sr:
            sr = sa[it][0]

        # Maintain the two largest Blue contributions.
        if sa[it][1] > fb:
            sb = fb
            fb = sa[it][1]
        elif sa[it][1] > sb:
            sb = sa[it][1]

    # Pass the best contribution excluding the current child
    # while rerooting the tree at every child.
    for it in adj[node]:
        if it == par:
            continue

        new_red = 0
        new_blue = 0

        if s[node] == 'R':
            # Use the best Red contribution
            # that does not come from this child.
            new_red = 1
            if sa[it][0] == fr:
                new_red += sr
            else:
                new_red += fr
            new_blue = 0
        else:
            # Use the best Blue contribution
            # that does not come from this child.
            new_red = 1
            if sa[it][1] == fb:
                new_red += sb
            else:
                new_red += fb
            new_blue = new_red

        # Reroot the tree at the current child.
        reroot(adj, s, ans, sa, it, node, new_red, new_blue)


def longestPath(s, edges):
    n = len(s)

    # Build the adjacency list of the tree.
    adj = [[] for _ in range(n)]

    for e in edges:
        adj[e[0] - 1].append(e[1] - 1)
        adj[e[1] - 1].append(e[0] - 1)

    # Index 0 represents Red and index 1 represents Blue.
    subTreeAns = [[0, 0] for _ in range(n)]

    # Calculate DP values using a bottom-up traversal.
    root(adj, s, subTreeAns)

    ans = [[0, 0] for _ in range(n)]

    # Reroot the tree to consider paths in all directions.
    reroot(adj, s, ans, subTreeAns)

    res = 0

    # Find the maximum valid path length.
    for i in range(n):
        res = max(res, ans[i][0], ans[i][1])

    return res


if __name__ == "__main__":
    s = "RBB"

    edges = [[1, 2], [1, 3]]

    print(longestPath(s, edges))
    
    
s = "RBB"
edges = [[1, 2], [1, 3]]
print(longestPath(s, edges))






