def dfs(node, adj, visited, res):
    visited[node] = 1
    
    for neighbor in adj[node]:
        if visited[neighbor] == 1:
            return False
        
        elif visited[neighbor] == 0:
            if not dfs(neighbor, adj, visited, res):
                return False
            
    visited[node] = 2
    res.append(node)
    return True

def findOrder(n, prerequisites):
    adj = [[] for _ in range(n)]
    
    for step in prerequisites:
        dest, src = step
        adj[src].append(dest)
        
    visited = [0] * n
    
    res = []
    for i in range(n):
        if visited[i] == 0:
            if not dfs(i, adj, visited, res):
                return []
            
    res.reverse()
    return res
        


n = 4
prerequisites = [[2, 0], [2, 1], [3, 2]]
print(findOrder(n, prerequisites))
