def maxEdgesToAdd(V, edges):
    n = len(edges)
    possible_edge = V * (V - 1) // 2
    
    return possible_edge - n
        


V = 4
E = 3
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
print(maxEdgesToAdd(V, edges))
