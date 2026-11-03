# Given a weighted tree with n nodes, numbered from 1 to n and n - 1 edges, where each edge is represented as [u, v, w] indicating an edge between nodes u and v with weight w.

# You are also given an array queries[], where each queries[i] represents a maximum allowed edge weight.

# For each query x, find the number of distinct paths in the tree such that the maximum edge weight along the path is less than or equal to x.

# Return an array containing the number of valid paths for each query.

# Note:

# A path from node u to node v and the path from node v to node u are considered the same path.
# A path must contain at least one edge. A path from a node to itself is not considered.

# DSU with Sorting and Map - O(n log n + q log n) Time and O(n) Space



from bisect import bisect_right

# Find the representative of a set.


def root(x, parent):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


# Union two components.
def union(a, b, parent, sz, ans):
    ra = root(a, parent)
    rb = root(b, parent)

    # Already in the same component.
    if ra == rb:
        return ans

    # Union by size.
    if sz[ra] < sz[rb]:
        ra, rb = rb, ra

    # Count paths between the two components.
    ans += sz[ra] * sz[rb]

    parent[rb] = ra
    sz[ra] += sz[rb]

    return ans


def maximumWeight(n, edges, queries):
    ans = 0

    parent = list(range(n + 1))
    sz = [1] * (n + 1)

    # Store (weight, u, v).
    wt = []

    for e in edges:
        wt.append((e[2], e[0], e[1]))

    # Sort edges by weight.
    wt.sort()

    # Store the number of valid paths for each weight.
    mp = {}
    i = 0

    while i < len(wt):
        weight = wt[i][0]

        # Process all edges having the same weight.
        while i < len(wt) and wt[i][0] == weight:
            u = wt[i][1]
            v = wt[i][2]

            ans = union(u, v, parent, sz, ans)
            i += 1

        # Store the answer after processing this weight.
        mp[weight] = ans

    # Sort the weights for binary search.
    weights = sorted(mp.keys())
    res = []

    # Process every query.
    for x in queries:
        pos = bisect_right(weights, x)

        if pos == 0:
            res.append(0)
        else:
            res.append(mp[weights[pos - 1]])

    return res


# Driver Code
if __name__ == "__main__":
    n = 7
    edges = [
        [1, 2, 3],
        [2, 3, 1],
        [2, 4, 9],
        [3, 6, 7],
        [3, 5, 8],
        [5, 7, 4]
    ]
    queries = [1, 3, 5]

    ans = maximumWeight(n, edges, queries)
    print(ans)
 

