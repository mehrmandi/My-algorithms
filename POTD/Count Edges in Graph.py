# Given an undirected graph with V vertices numbered from 0 to V - 1, represented by an adjacency list adj[][], where adj[i] contains the vertices adjacent to vertex i.

# Return the total number of edges present in the graph.


# Handshaking Lemma - O(V + E) Time and O(1) Space
def countEdges(adj):
    sum = 0

    # Traverse all vertices and add the size of their adjacency lists
    for neighbors in adj:
        sum += len(neighbors)

    # Each edge is counted twice in an undirected graph
    return sum // 2




adj = [[1], [0, 2], [1, 3], [2]]
print(countEdges(adj))
        
