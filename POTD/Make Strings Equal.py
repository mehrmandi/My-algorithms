import sys


def min_cost_to_make_identical(s, t, transform, cost):
    INF = float('inf')
    n = 26  # lowercase letters
    dist = [[INF] * n for _ in range(n)]

    # Initialize distances
    for i in range(n):
        dist[i][i] = 0

    for (a, b), c in zip(transform, cost):
        dist[ord(a) - ord('a')][ord(b) - ord('a')
                                ] = min(dist[ord(a) - ord('a')][ord(b) - ord('a')], c)

    # Floyd-Warshall to find all-pairs shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    if len(s) != len(t):
        return -1

    total_cost = 0
    for a, b in zip(s, t):
        if a == b:
            continue
        min_pair_cost = INF
        for c in range(n):
            cost_a = dist[ord(a) - ord('a')][c]
            cost_b = dist[ord(b) - ord('a')][c]
            if cost_a != INF and cost_b != INF:
                min_pair_cost = min(min_pair_cost, cost_a + cost_b)
        if min_pair_cost == INF:
            return -1
        total_cost += min_pair_cost

    return total_cost
        
    
s = "abcc"
t = "bccc"
transform = [['a', 'b'], ['b', 'c'], ['c', 'a']]
cost = [2, 1, 4]
print(minCost(s, t, transform, cost))
