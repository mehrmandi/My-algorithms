# Time Complexity: O(V+E)-----------------------
# Auxiliary Space: O(V+E)-----------------------

def bfs(node, adj, visited, island):
    q = [node]
    
    while q:
        sz = len(q)
        
        for i in range(sz):
            curr = q.pop()
            if not visited[curr]:
                visited[curr] = True
            else:
                continue
            
            for neighbor in adj[curr]:
                q.append(neighbor)
    
    island[0] += 1
            
                

def minConnect(V, edges):
    adj = [[] for _ in range(V)]
    
    for edge in edges:
        u, v = edge[0], edge[1]
        adj[u].append(v)
        adj[v].append(u)
    
    E = len(edges)
    visited = [False for _ in range(V)]
    island = [0]
    
    
    if E < V - 1:
        return -1
    
    for node in range(V):
        if not visited[node]:
            bfs(node, adj, visited, island)
        else:
            continue
    
    return island[0] - 1

V = 5
E = 4
edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
print(minConnect(V, edges))



# Time Complexity: O(V+E)--------------------------
# Auxiliary Space: O(V+E)--------------------------


# DFS function to visit all hospitals in a connected component
# def dfs(start, adj, visited):
#     visited[start] = True
#     for neighbor in adj[start]:
#         if not visited[neighbor]:
#             dfs(neighbor, adj, visited)


# def minConnect(adj):
#     V = len(adj)
#     visited = [False] * V
#     edges = 0

#     # Count total number of edges
#     for i in range(V):
#         edges += len(adj[i])
#     edges //= 2

#     # Count disconnected components using DFS
#     components = 0
#     for i in range(V):
#         if not visited[i]:
#             components += 1
#             dfs(i, adj, visited)

#     # If total edges are less than (V - 1), it's impossible to connect all
#     if edges < V - 1:
#         return -1

#     # Calculate redundant (extra) edges
#     extra = edges - (V - components)

#     # If enough extra edges exist to connect all components
#     if extra >= (components - 1):
#         return components - 1

#     return -1


# if __name__ == "__main__":
#     adj = [[1, 2], [0, 2], [0, 1], []]

#     print(minConnect(adj))

# [Approach 1] Using Disjoint Set-----------------------------
# Time Complexity: O(V+E)
# Auxiliary Space: O(V+E)

# class DisjointSet:
#     def __init__(self, n):
#         self.rank = [0] * (n + 1)
#         self.parent = [i for i in range(n + 1)]
#         self.size = [1] * (n + 1)

#     # Find the ultimate parent of a node (with path compression)
#     def findUPar(self, node):
#         if node == self.parent[node]:
#             return node
#         self.parent[node] = self.findUPar(self.parent[node])
#         return self.parent[node]

#     # Union by size
#     def unionBySize(self, u, v):
#         ulpU = self.findUPar(u)
#         ulpV = self.findUPar(v)
#         if ulpU == ulpV:
#             return

#         if self.size[ulpU] < self.size[ulpV]:
#             self.parent[ulpU] = ulpV
#             self.size[ulpV] += self.size[ulpU]
#         else:
#             self.parent[ulpV] = ulpU
#             self.size[ulpU] += self.size[ulpV]

# # Function to find minimum operations required
# def minConnect(adj):
#     n = len(adj)
#     ds = DisjointSet(n)
#     extra = 0

#     # Traverse all links in adjacency list
#     for u in range(n):
#         for v in adj[u]:

#             # To avoid processing duplicate edges 
#             if u < v:

#                 # If both hospitals are already connected,
#                 #mark this link as extra
#                 if ds.findUPar(u) == ds.findUPar(v):
#                     extra += 1
#                 else:
#                     ds.unionBySize(u, v)

#     # Count disconnected components using DFS
#     components = sum(1 for i in range(n) if ds.findUPar(i) == i)

#     # If enough extra links exist to connect all components
#     if extra >= components - 1:
#         return components - 1
#     else:
#         return -1


# if __name__ == "__main__":
    
#     # Adjacency list
#     adj = [[1, 2],[0, 2],[0, 1],[]]

#     print(minConnect(adj))




