# Geek Town has n houses numbered from 1 to n, choose a house to host a party such that the distance from the party house to its farthest house is as small as possible. Return this minimum possible distance.

# The houses are connected by n − 1 bidirectional roads, forming a tree.
# The connections are given as an adjacency list adj, where adj[i] contains all houses directly connected to house i + 1.

# Tree Diameter using Two BFS - O(n) Time and O(n) Space

from collections import deque

def bfs(adj, start):
    n = len(adj)

    dist = [-1] * n
    q = deque()

    dist[start] = 0
    q.append(start)

    farthest_node = start
    farthest_dist = 0

    while q:
        node = q.popleft()

        for next_node in adj[node]:

            # Convert 1-based house number
            # to 0-based index.
            next_node -= 1

            if dist[next_node] == -1:

                dist[next_node] = dist[node] + 1
                q.append(next_node)

                # Update the farthest house.
                if dist[next_node] > farthest_dist:
                    farthest_dist = dist[next_node]
                    farthest_node = next_node

    return farthest_node, farthest_dist



def partyHouse(adj: list[list[int]]) -> int:
    # First BFS:
    # Find one endpoint of the diameter.
    diameter_end, _ = bfs(adj, 0)

    # Second BFS:
    # Find the diameter length.
    _, diameter = bfs(adj, diameter_end)

    # The optimal party house lies at the center
    # of the diameter.
    # ceil(diameter / 2) = (diameter + 1) // 2
    return (diameter + 1) // 2
    

adj = [[2], [1, 4, 3], [2], [2]]
print(partyHouse(adj))
