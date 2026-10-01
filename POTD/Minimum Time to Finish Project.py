# An IT company is working on a large project consisting of n modules.

# The given array time required ( in months) to complete the ith module is stored in the array duration[].
# The array dependencies[][], where dependencies[i] = [u, v], indicates that module v can be started only after module u is completed.
# Multiple modules can be worked on simultaneously as long as all their dependencies have been completed.

# Find the minimum time required to complete the entire project.

# If the project cannot be completed due to a cyclic dependency, return -1.
# A module is never dependent on itself.

# Using Topological Sort with DP - O(n + m) Time and O(n + m) Space



from collections import deque

def minTime(duration, dependencies):
    n = len(duration)
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    time = duration[:]
    
    for u, v in dependencies:
        adj[u].append(v)
        indegree[v] += 1
        
    q = deque()
    
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
            time[i] = duration[i]
            
    count = 0
    
    while q:
        node = q.popleft()
        count += 1

        for v in adj[node]:
            time[v] = max(time[v], time[node] + duration[v])
            
            indegree[v] -= 1
            
            if indegree[v] == 0:
                q.append(v)
                
    if count != n:
        return -1
    
    return max(time)     
    
    
duration = [10, 20, 30, 10, 30, 20]
dependencies = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
print(minTime(duration, dependencies))
    
    
