
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)
    

def farthestNode(curr, adj, currentDist, dist, visited):
    if visited[curr]:
        return
    if dist[0] < currentDist:
        # contains an array with index 0
        # having max dist and index 1 having
        # node at that distance from src
        dist[0] = currentDist
        dist[1] = curr
    visited[curr] = True
    for next_node in adj[curr]:
        if not visited[next_node]:
            farthestNode(next_node, adj, currentDist + 1, dist, visited)


def diameter(V, edges):
    adj = [[] for _ in range(V)]
    
    for edge in edges:
        addEdge(adj, edge[0], edge[1])
        
    n = len(adj) + 1
    dist = [0, 0]
    # finding node at max distance from 0th node
    farthestNode(0, adj, 0, dist, [False] * n)
    end1 = dist[1]

    dist = [0, 0]
    # finding node at max distance
    # from end1 of diameter
    farthestNode(end1, adj, 0, dist, [False] * n)
    return dist[0]
          
        
        
V = 7
E = 5
edges = [[0, 2], [0, 4], [0, 3], [3, 1], [3, 5], [1, 6]]
print(diameter(V, edges))
